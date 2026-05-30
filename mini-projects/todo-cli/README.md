# ToDo-CLI

## Project Overview

ToDo-CLI is a command-line task management application that allows users to create, view, delete, save, and load tasks. The project demonstrates modular programming, file persistence, and basic CRUD operations using Python.

## Features

- Add Task -> Add a new task to memory
- View Tasks -> Display all current tasks
- Delete Task -> Remove a task using its index
- Menu -> Display available commands
- Save Tasks -> Save tasks to a file
- Load Tasks -> Load saved tasks from a file
- Clear Tasks -> Remove tasks from memory only
- Reset -> Remove tasks from memory and file
- Exit -> Terminate the program

## Architecture

```text
main.py
├── Menu handling
├── User input
└── Program flow

tasks.py
├── Add task
├── View tasks
└── Delete task

storage.py
├── Save tasks
├── Load tasks
└── Reset tasks

tasks.txt
└── Persistent task storage
```

## How to Run

```bash
python main.py
```

## Concepts Learned

- Functions
- File Handling
- Persistence
- CRUD Operations
- Modules
- State Management
- User Feedback
- Separation of Concerns

## Example Session

```text
Enter Operation: add
Enter Task: Learn Python

Enter Operation: add
Enter Task: Learn Git

Enter Operation: view

1. Learn Python
2. Learn Git
```
