# Task Management System

## Introduction

This is a task management system that allows users to create, assign, prioritize, and track the progress of tasks. It also supports task dependencies and collaborative commenting.

## User Stories

1. **Create a Task:**
   - As a user, I want to be able to create a new task.
   - Acceptance Criteria:
     - The system should generate a unique task identifier.
     - Each task should have a title, description, and a status (e.g., To-Do, In Progress, Done).
   - Tasks:
     1. Implement a `Task` class with properties for task identifier, title, description, and status.
     2. Utilize the Factory Method design pattern to create different types of tasks.
     3. Write a test to ensure that the task identifier generated is unique.

2. **Assign and Update Tasks:**
   - As a project manager, I want to assign tasks to team members and update their status.
   - Acceptance Criteria:
     - Tasks can be assigned to specific team members.
     - The status of a task can be updated (e.g., from To-Do to In Progress, from In Progress to Done).
   - Tasks:
     1. Add methods to the `Task` class for assigning team members and updating task status.
     2. Implement the Observer design pattern to notify relevant stakeholders of task updates.
     3. Write tests to verify that task assignments and status updates are handled correctly.

3. **Task Priority:**
   - As a user, I want to prioritize tasks based on their urgency.
   - Acceptance Criteria:
     - Tasks can have different priority levels (e.g., High, Medium, Low).
     - The system should allow users to sort and filter tasks based on priority.
   - Tasks:
     1. Add a priority property to the `Task` class.
     2. Implement a Strategy design pattern to handle different prioritization strategies.
     3. Write tests to ensure that tasks can be sorted and filtered based on priority.

4. **Task Dependencies:**
   - As a user, I want to define dependencies between tasks.
   - Acceptance Criteria:
     - A task can have one or more dependencies on other tasks.
     - The system should prevent closing a task with unresolved dependencies.
   - Tasks:
     1. Add a dependencies property to the `Task` class.
     2. Implement a Command design pattern to handle task dependencies.
     3. Write tests to ensure that tasks with unresolved dependencies cannot be closed.

5. **Task Comments:**
   - As a team member, I want to add comments to tasks for collaboration.
   - Acceptance Criteria:
     - Users can add comments to tasks to discuss details or provide updates.
     - The system should display the comment history for each task.
   - Tasks:
     1. Implement a `Comment` class with properties for author, timestamp, and content.
     2. Use the Observer pattern to update the comment history when new comments are added.
     3. Write tests to verify that comments can be added and displayed correctly.

## Development Setup

1. Clone the repository: `git clone [repository-url]`

## Running Tests
