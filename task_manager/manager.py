"""Core logic for managing a list of tasks."""
from task_manager.task import Task


class TaskManager:
    """Keeps tasks in memory and hands out unique identifiers."""

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        """Add a new task and return it."""
        task = Task(id=self.next_id, title=title)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self):
        """Return all tasks in the order they were added."""
        return list(self.tasks)

    def get_task(self, task_id):
        """Return the task with the given id, or None."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def complete_task(self, task_id):
        """Mark a task as completed (implemented on feature/complete-task)."""
        raise NotImplementedError("Completing tasks is not implemented yet")

    def pending_count(self):
        """Number of tasks that are not completed yet."""
        return sum(1 for task in self.tasks if not task.completed)

    def delete_task(self, task_id):
        """Delete a task (implemented on feature/delete-task)."""
        raise NotImplementedError("Deleting tasks is not implemented yet")
