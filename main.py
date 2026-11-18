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
    task = manager.add_task(title)
    print(f"Added task {task.id}: {task.title}")


def handle_display(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        print(task)
    print(f"{manager.pending_count()} task(s) pending")


def handle_complete(manager):
    print("Completing tasks is coming soon.")


def handle_delete(manager):
    print("Deleting tasks is coming soon.")


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
