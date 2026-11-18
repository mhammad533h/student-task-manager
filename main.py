"""Console interface for the Student Task Manager."""
from task_manager.manager import TaskManager
from task_manager.storage import load_tasks, save_tasks

MENU = """
===== Student Task Manager =====
1. Add task
2. Display tasks
3. Complete task
4. Delete task
5. Exit
"""


def handle_add(manager):
    title = input("Task title: ")
    try:
        task = manager.add_task(title)
    except ValueError as error:
        print(f"Error: {error}")
        return
    print(f"Added task {task.id}: {task.title}")


def handle_display(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        print(task)
    print(f"{manager.pending_count()} task(s) pending")


def read_task_id(prompt):
    """Ask for a task id and return it as an int, or None if invalid."""
    raw = input(prompt).strip()
    if not raw.isdigit():
        print("Error: please enter a numeric task id.")
        return None
    return int(raw)


def handle_complete(manager):
    task_id = read_task_id("Task id to complete: ")
    if task_id is None:
        return
    try:
        task = manager.complete_task(task_id)
    except ValueError as error:
        print(f"Error: {error}")
        return
    print(f"Task {task.id} marked as completed.")


def handle_delete(manager):
    raw = input("Task id to delete: ").strip()
    if not raw.isdigit():
        print("Error: please enter a numeric task id.")
        return
    try:
        task = manager.delete_task(int(raw))
    except ValueError as error:
        print(f"Error: {error}")
        return
    print(f"Deleted task {task.id}: {task.title}")


def main():
    manager = TaskManager()
    load_tasks(manager)
    actions = {"1": handle_add, "2": handle_display, "3": handle_complete, "4": handle_delete}
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid option, please choose 1-5.")
            continue
        action(manager)
        save_tasks(manager)


if __name__ == "__main__":
    main()
