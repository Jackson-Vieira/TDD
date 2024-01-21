from django.test import TestCase

from .models import Task

from django.urls import reverse


class TaskModelTest(TestCase):
    def test_tasks_models_exists(self):
        tasks = Task.objects.count()
        self.assertEqual(tasks, 0)

    def test_model_has_string_representation(self):
        task = Task.objects.create(title="test")
        self.assertEqual(str(task), "test")


class IndexPageTest(TestCase):
    def setUp(self) -> None:
        self.list_tasks_url = reverse("task:list_tasks")
        self.task = Task.objects.create(title="test")

    def test_index_page_returns_correct_response(self):
        response = self.client.get(self.list_tasks_url)
        self.assertTemplateUsed(response, "task/index.html")
        self.assertEqual(response.status_code, 200)

    def test_index_page_has_tasks(self):
        response = self.client.get(self.list_tasks_url)
        self.assertContains(response, self.task.title)

    def test_index_page_list_all_tasks(self):
        Task.objects.create(title="test2")
        response = self.client.get(self.list_tasks_url)
        self.assertContains(response, self.task.title)
        self.assertContains(response, "test2")


class DetailPageTest(TestCase):
    def setUp(self) -> None:
        self.task = Task.objects.create(
            title="test title", description="test description"
        )

    def _get_page_url(self, task_id: int = 1) -> str:
        return reverse("task:task_detail", args=[task_id])

    def test_detail_page_returns_correct_response(self):
        response = self.client.get(self._get_page_url())
        self.assertTemplateUsed(response, "task/detail.html")
        self.assertEqual(response.status_code, 200)

    def test_detail_page_contains_task(self):
        response = self.client.get(self._get_page_url(self.task.id))
        self.assertContains(response, self.task.title)
        self.assertContains(response, self.task.description)

    def test_detail_page_invalid_task_id(self):
        response = self.client.get(self._get_page_url(999))
        self.assertEquals(response.status_code, 404)


class DeleteTaskTest(TestCase):
    def setUp(self) -> None:
        self.task = Task.objects.create(
            title="test title", description="test description"
        )

    def test_delete_task(self):
        response = self.client.post(reverse("task:task_delete", args=[self.task.id]))
        self.assertEquals(Task.objects.count(), 0)
        self.assertRedirects(response, reverse("task:list_tasks"))

    def test_delete_task_invalid_id(self):
        response = self.client.post(reverse("task:task_delete", args=[999]))
        self.assertEquals(Task.objects.count(), 1)
        self.assertEqual(response.status_code, 404)

    def test_delete_task_with_invalid_http_method(self):
        response = self.client.get(reverse("task:task_delete", args=[1]))
        self.assertEqual(response.status_code, 405)
        self.assertEquals(Task.objects.count(), 1)

        response = self.client.put(reverse("task:task_delete", args=[1]))
        self.assertEqual(response.status_code, 405)
        self.assertEquals(Task.objects.count(), 1)
