import math
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def floor_divide(a,b):
    return a//b
def modulus(a,b):
    return a%b
def power(a,b):
    return math.pow(a,b)
def save_history(history):
    with open("history.txt","w") as file:
        for i in history:
            file.write(i+'\n')
    print("History saved")
def load_history(history):
    try:
        with open("history.txt","r") as file:
            history.clear()
            for i in file:
                history.append(i.strip())
        print("History loaded")
    except FileNotFoundError:
        print("No saved history found!")
def clear_history(history):
    history.clear()
    with open("history.txt","w") as file:
        pass
    print("History cleared!")
def menu():
    print("Enter 'exit' to terminate the program")
    print("Enter 'history' to display calculation history")
    print("Input example for calculation: '5 + 3'")
    print("Enter 'history' to view previous calculations")
    print("Enter 'load' to log data into history")
    print("Enter 'save' to save history")
    print("Enter 'clear' to clear history")
history=[]
operations={'+':add, '-': subtract, '*': multiply, '/': divide,'//': floor_divide, '%':modulus, '^': power}
print("Enter 'menu' for details")
while True:
    try:
        user_input=input(">>>").strip()
        if user_input.lower()=="menu":
            menu()
        elif user_input.lower()=="history":
            if history:
                for i in history:
                    print(i)
            else:
                print("No history found")
        elif user_input.lower()=="save":
            save_history(history)
        elif user_input.lower()=="load":
            load_history(history)
        elif user_input.lower()=="clear":
            clear_history(history)
        elif user_input.lower()=="exit":
            break
        else:
            a,s,b=user_input.split()
            a,b=float(a),float(b)
            if s in operations:
                if s in ['/','//','%'] and b==0:
                    print("Division by zero not possible")
                else:
                    result=operations[s](a,b)
                    exp=f"{a} {s} {b} = {result}"
                    history.append(exp)
                    print(result)
            else:
                print("Invalid operator")
    except ValueError:
        print("Invalid input. Try format: 5 + 3")
print("Program Terminated")