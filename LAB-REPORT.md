# Lab Report - Assignment 4

**Course:** CSC418 DevOps for Cloud Computing
**Student:** MUHAMMAD HAMMAD (GitHub: [mhammad533h](https://github.com/mhammad533h))
**Repository:** https://github.com/mhammad533h/student-task-manager
**Release:** https://github.com/mhammad533h/student-task-manager/releases/tag/v1.0.0

## Summary of what was done

| Requirement | Evidence in this repository |
|---|---|
| 12+ meaningful commits | `git log` on `main` (see `lab-evidence/`) |
| 3 feature branches | `feature/add-task`, `feature/complete-task`, `feature/delete-task` (plus `feature/tests-ci`, `docs/user-guide-and-report`) |
| 4+ Issues with labels | Issues #1 - #5 (enhancement, validation, testing, documentation) |
| 5 merged Pull Requests | PRs for the three features, tests + CI, and documentation |
| 1 resolved merge conflict | `status/in-progress` vs `status/testing` on the README status line |
| 3+ automated tests | `tests/test_task_manager.py` (5 tests) |
| 1 workflow | `.github/workflows/tests.yml` - one failed run and one successful run |
| 1 release | `v1.0.0` |

## 1. Git vs GitHub; add, commit and push

**Git** is a version control tool that runs on my own computer. It records snapshots of the
project, keeps the full history and lets me create branches and merge them, even offline.
**GitHub** is a website that hosts Git repositories online and adds collaboration features
on top: Issues, Pull Requests, code review, GitHub Actions and Releases.

- `git add` moves changes into the *staging area*, so I choose exactly what goes into the next commit.
- `git commit` saves the staged changes as a permanent snapshot in the local history with a message explaining why.
- `git push` uploads my local commits to the remote repository on GitHub so others (and CI) can see them.

## 2. Why branches and Pull Requests; what causes merge conflicts

A **branch** is an independent line of development. I built each feature (add, complete,
delete) on its own branch, so unfinished work never broke `main`, and each feature could be
reviewed and merged separately.

A **Pull Request** asks to merge one branch into another. It shows the changed files, lets
teammates comment on specific lines, links the related Issue, and runs the automated tests
before anything reaches `main`.

A **merge conflict** happens when two branches change *the same lines* of the same file in
different ways, so Git cannot decide which version to keep. In this lab, `status/in-progress`
changed the README line to `Project status: In progress` and `status/testing` changed the
same line to `Project status: Testing`. After the first branch was merged, merging the second
produced conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`). I edited the line by hand to
`Project status: In progress - testing phase`, removed the markers, then ran `git add` and
`git commit` to finish the merge. No other lines of the README were touched.

## 3. fetch vs pull; merge vs rebase

- `git fetch` downloads new commits from the remote but **does not change** my working files
  or current branch; I can inspect them first (for example with `git log origin/main`).
- `git pull` is `git fetch` **followed by** a merge (or rebase) into my current branch, so my
  files are updated immediately.

- `git merge` joins two branches by creating a **merge commit**. History is preserved exactly
  as it happened, so the graph shows where branches split and joined.
- `git rebase` **replays** my commits on top of another branch, creating new commits and a
  straight, linear history. It is cleaner to read but rewrites history, so it should not be
  used on branches other people already pulled.

## 4. How Issues and Actions help a team

**GitHub Issues** act as a shared to-do list: each bug, feature or documentation task gets a
number, description, labels and an owner. Pull Requests can reference an Issue (`Closes #1`)
so it closes automatically when the work is merged, which makes it easy to see what is done.

**GitHub Actions** runs automated jobs on GitHub's servers. My workflow runs the unit tests on
every push and Pull Request to `main`. When a test failed, the PR showed a red ✗ before
merging, so broken code was caught automatically instead of by a teammate later.

## 5. A difficulty I faced and how I solved it

My first GitHub Actions run on the tests Pull Request **failed**. The log showed
`test_complete_task` failing with `AssertionError: 0 != 1`. I had written the test to expect
one pending task after completing the only task in the list, which was wrong: after completing
it, zero tasks are pending. I fixed the expected value in the test, pushed the commit to the
same branch, and the workflow re-ran automatically and passed. This showed me why CI is useful:
the mistake was caught in the Pull Request before anything was merged into `main`.
