"""Save and load tasks as JSON so they survive between runs."""
import json
import os

from task_manager.task import Task

DEFAULT_FILE = "tasks.json"


def save_tasks(manager, path=DEFAULT_FILE):
    data = {"next_id": manager.next_id, "tasks": [t.to_dict() for t in manager.tasks]}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_tasks(manager, path=DEFAULT_FILE):
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    manager.tasks = [Task.from_dict(item) for item in data.get("tasks", [])]
    manager.next_id = data.get("next_id", len(manager.tasks) + 1)
