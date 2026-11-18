"""Core logic for managing a list of tasks."""
from task_manager.task import Task


class TaskManager:
    """Keeps tasks in memory and hands out unique identifiers."""

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    MAX_TITLE_LENGTH = 100

    def add_task(self, title):
        """Add a new task and return it.

        Raises ValueError if the title is empty or too long.
        """
        title = (title or "").strip()
        if not title:
            raise ValueError("Task title cannot be empty")
        if len(title) > self.MAX_TITLE_LENGTH:
            raise ValueError(f"Task title must be at most {self.MAX_TITLE_LENGTH} characters")
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
        """Mark the task with the given id as completed and return it.

        Raises ValueError if no task has that id.
        """
        task = self.get_task(task_id)
        if task is None:
            raise ValueError(f"No task with id {task_id}")
        task.completed = True
        return task

    def pending_count(self):
        """Number of tasks that are not completed yet."""
        return sum(1 for task in self.tasks if not task.completed)

    def delete_task(self, task_id):
        """Delete a task (implemented on feature/delete-task)."""
        raise NotImplementedError("Deleting tasks is not implemented yet")
