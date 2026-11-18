# Student Task Manager - User Guide

## Starting the program

Open a terminal in the project folder and run:

```bash
python main.py
```

The main menu appears:

```
===== Student Task Manager =====
1. Add task
2. Display tasks
3. Complete task
4. Delete task
5. Exit
```

## 1. Adding a task

Choose `1` and type a title, for example `Submit DevOps lab`.
The program replies with the new task's id: `Added task 1: Submit DevOps lab`.
An empty title is rejected with `Error: Task title cannot be empty`.

## 2. Displaying tasks

Choose `2` to list all tasks:

```
[ ] 1. Submit DevOps lab
[x] 2. Read chapter 4
1 task(s) pending
```

`[x]` means completed, `[ ]` means still pending.

## 3. Completing a task

Choose `3` and enter the task id shown in the list. The task is marked `[x]`.
A non-numeric or unknown id shows an error and nothing changes.

## 4. Deleting a task

Choose `4` and enter the task id. The task is removed from the list.
Ids of other tasks do not change.

## 5. Exiting

Choose `5`. Tasks are saved automatically to `tasks.json` after every action,
so they are still there the next time you start the program.

## Troubleshooting

| Problem | Fix |
|---|---|
| `python: command not found` | Use `python3 main.py` instead |
| Want to start with an empty list | Delete the `tasks.json` file |
