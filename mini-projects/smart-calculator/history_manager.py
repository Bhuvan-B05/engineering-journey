# History Management
def save_history(history): # Write History to file for longer access
    with open("history.txt","w") as file:
        for i in history:
            file.write(i+'\n')
    print("History saved")

def load_history(history): # Load history from file to list
    try:
        with open("history.txt","r") as file:
            history.clear()
            for i in file:
                history.append(i.strip())
        print("History loaded")
    except FileNotFoundError:
        print("No saved history found!")


def clear_history(history): # Clear history from file and list
    history.clear()
    with open("history.txt","w") as file:
        pass
    print("History cleared!")