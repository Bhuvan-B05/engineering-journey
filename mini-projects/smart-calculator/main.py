import math
from datetime import datetime # for timestamps in history

# Arithmetic Operations
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        raise ValueError("Division By Zero not possible")
    return a/b
def floor_divide(a,b):
    if b==0:
        raise ValueError("Division By Zero not possible")
    return a//b
def modulus(a,b):
    if b==0:
        raise ValueError("Division By Zero not possible")
    return a%b
def power(a,b):
    return math.pow(a,b)

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

# User Interface
def menu(): # Display menu of  Commands
    print("\n===== SMART CALCULATOR MENU =====")
    print("Enter calculations in this format:")
    print("5 + 3")
    print("\nCommands:")
    print("menu     -> Show menu")
    print("history  -> Display history")
    print("save     -> Save history")
    print("load     -> Load history")
    print("clear    -> Clear history")
    print("exit     -> Exit calculator")

# Handles commands
def process_command(user_input,history,operations):
    if user_input.lower()=="menu":
            menu()
            return True
    elif user_input.lower()=="history":
        if history:
            for i in history:
                print(i)
        else:
            print("No history found")
        return True
    elif user_input.lower()=="save":
        save_history(history)
        return True
    elif user_input.lower()=="load":
        load_history(history)
        return True
    elif user_input.lower()=="clear":
        clear_history(history)
        return True
    elif user_input.lower()=="exit":
        return False
    calculation(user_input,history,operations)
    return True

# Handles calculations
def calculation(user_input,history,operations):
    try: # Exception handling for invalid input

        parts=user_input.split() # parsing input
        if len(parts)!=3:
            raise ValueError("Input format should be: number operator number")
        a,s,b=parts
        a,b=float(a),float(b)
        if a.is_integer():
            a=int(a)
        if b.is_integer():
            b=int(b)
        if s in operations:
            result=operations[s](a,b)

            if isinstance(result,float) and result.is_integer():
                result=int(result)

            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            exp=f"[{timestamp}] {a} {s} {b} = {result}"

            history.append(exp)

            print(result)
        else:
            print("Invalid operator")
    except ValueError as e:
        print(e)

# main function
history=[]
operations={'+':add, '-': subtract, '*': multiply, '/': divide,'//': floor_divide, '%':modulus, '^': power}
print("Enter 'menu' for details")
while True:
     user_input=input(">>>").strip()
     if not process_command(user_input,history,operations):
        break
print("Program Terminated")