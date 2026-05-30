from tasks import add_task,view_tasks,delete_task
from storage import save_tasks,load_tasks,clear_tasks,reset

def menu():
    print("===============================")
    print("             Menu              ")
    print("===============================")
    print("Available Features:\n")
    print("1. Add Task -> add")
    print("2. View Tasks -> view")
    print("3. Delete Task -> delete -> enter index")
    print("4. View Menu -> menu")
    print("5. Save Tasks -> save")
    print("6. Load Tasks -> load")
    print("7. Clear Tasks from memory -> clear")
    print("8. Reset (remove tasks from memory and file) -> reset")
    print("9. Exit -> exit\n")

tasks=[]
menu()
while True:
    inp=input("Enter Operation:").lower()
    if inp=="add":
        task=input("Enter Task: ")
        add_task(tasks,task)
    elif inp=="view":
        view_tasks(tasks)
    elif inp=="delete":
        try:
            idx=int(input("Enter the task number to be deleted: "))
        except ValueError:
            print("Please enter a valid number\n")
        delete_task(tasks,idx-1)
    elif inp=="menu":
        menu()
    elif inp=="save":
        save_tasks(tasks)
    elif inp=="load":
        load_tasks(tasks)
    elif inp=="clear":
        clear_tasks(tasks)
    elif inp=="reset":
        reset(tasks)
    elif inp=="exit":
        break
    else:
        print("Invalid command! Please refer menu\n")
print("Program Termminated")

