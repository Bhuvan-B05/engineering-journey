def add_task(tasks,task):
    if not task.strip():
        print("Task cannot be empty\n")
        return
    tasks.append(task)
    print("Task added\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found\n")
        return

    for i,task in enumerate(tasks,start=1):
        print(f"{i}. {task}")
    print("\n")

def delete_task(tasks,index):
    if 0<= index<len(tasks):
        removed=tasks.pop(index)
        print(f"Task deleted: {removed}\n")
    else:
        print("Invalid task number\n")