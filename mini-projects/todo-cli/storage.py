def save_tasks(tasks):
    with open("tasks.txt","w") as file:
        for i in tasks:
            file.write(i+"\n")
    print("Tasks saved successfully\n")

def load_tasks(tasks):
    try:
        with open("tasks.txt","r") as file:
            tasks.clear()
            for i in file:
                tasks.append(i.strip())
        print("Tasks loaded successfully\n")
    except FileNotFoundError:
        print("No saved tasks found\n")

def clear_tasks(tasks):
    tasks.clear()
    print("Tasks removed from memory\n")

def reset(tasks):
    tasks.clear()
    with open("tasks.txt","w") as file:
        pass
    print("All saved tasks are removed\n")