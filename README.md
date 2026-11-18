# Student Task Manager

A small Python console application for students to keep track of their tasks.
Built for **CSC418 DevOps for Cloud Computing - Lab Assignment 4** to practice a full
Git and GitHub workflow (commits, branches, pull requests, merge conflicts, CI and releases).

Project status: In progress - testing phase

![Python tests](https://github.com/mhammad533h/student-task-manager/actions/workflows/tests.yml/badge.svg)

## Features

- **Add tasks** - empty or whitespace-only titles are rejected, titles are limited to 100 characters
- **Display tasks** - shows every task with a `[x]` / `[ ]` completion mark and the number still pending
- **Complete tasks** - mark a task as done using its numeric id
- **Delete tasks** - remove a task using a valid id; unknown ids show an error
- **Saved between runs** - tasks are stored in `tasks.json` (ignored by Git)
- **Automated tests** - `unittest` suite run by GitHub Actions on every push and pull request to `main`

## Project structure

```
student-task-manager/
├── main.py                  # console menu (entry point)
├── task_manager/
│   ├── task.py              # Task data class
│   ├── manager.py           # TaskManager: add / list / complete / delete
│   └── storage.py           # save and load tasks.json
├── tests/
│   └── test_task_manager.py # unit tests
├── docs/user-guide.md       # short user guide
├── lab-evidence/            # screenshots of each lab step
├── LAB-REPORT.md            # answers to the lab report questions
└── .github/workflows/tests.yml
```

## Setup

Requirements: Python 3.8 or newer and Git. No third-party packages are needed.

```bash
git clone https://github.com/mhammad533h/student-task-manager.git
cd student-task-manager
```

## Usage

```bash
python main.py
```

```
===== Student Task Manager =====
1. Add task
2. Display tasks
3. Complete task
4. Delete task
5. Exit
```

Choose an option by typing its number. See [docs/user-guide.md](docs/user-guide.md) for a walkthrough.

## Running the tests

```bash
python -m unittest discover -s tests -v
```

The same command runs automatically in GitHub Actions (`.github/workflows/tests.yml`)
on every push to `main` and on every pull request targeting `main`.

## License

Released under the [MIT License](LICENSE).
