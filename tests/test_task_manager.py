"""Unit tests for the Student Task Manager."""
import unittest

from task_manager.manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Finish DevOps lab")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Finish DevOps lab")
        self.assertFalse(task.completed)
        self.assertEqual(len(self.manager.list_tasks()), 1)

    def test_add_task_rejects_empty_title(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")
        self.assertEqual(self.manager.list_tasks(), [])

    def test_complete_task(self):
        task = self.manager.add_task("Read chapter 4")
        self.manager.complete_task(task.id)
        self.assertTrue(self.manager.get_task(task.id).completed)
        self.assertEqual(self.manager.pending_count(), 1)

    def test_delete_task(self):
        first = self.manager.add_task("Task one")
        second = self.manager.add_task("Task two")
        self.manager.delete_task(first.id)
        self.assertEqual(self.manager.list_tasks(), [second])
        self.assertIsNone(self.manager.get_task(first.id))

    def test_delete_unknown_task_raises(self):
        with self.assertRaises(ValueError):
            self.manager.delete_task(99)


if __name__ == "__main__":
    unittest.main()
