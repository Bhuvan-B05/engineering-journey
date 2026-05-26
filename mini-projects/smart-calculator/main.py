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
def factorial(value):
    if not isinstance(value, int):
        raise ValueError("Factorial only works with integers")

    if value < 0:
        raise ValueError("Factorial not defined for negative numbers")
    return math.factorial(value)

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
def menu():# Display Menu of commands
    print("\n===== SMART CALCULATOR MENU =====")
    print("Enter calculations in these formats:")
    print("   • Binary operations: 5 + 3, 10 - 2, 4 * 7, 8 / 2, 9 // 2, 10 % 3, 2 ^ 5")
    print("   • Unary operations : sqrt 25, abs -12, sin 1.57, cos 0, tan 0.78, fact 5")
    print("   • Trigonometric functions use radians")
    print("\nCommands:")
    print("   menu     -> Show menu")
    print("   history  -> Display history")
    print("   save     -> Save history")
    print("   load     -> Load history")
    print("   clear    -> Clear history")
    print("   exit     -> Exit calculator")


# Handles commands
def process_command(user_input,history,un_ops,bin_ops):
    cmd = user_input.lower()
    if cmd=="menu": menu(); return True
    elif cmd=="history":
        print("\n".join(history) if history else "No history found")
        return True
    elif cmd=="save": save_history(history); return True
    elif cmd=="load": load_history(history); return True
    elif cmd=="clear": clear_history(history); return True
    elif cmd=="exit": return False
    calculation(user_input,history,un_ops,bin_ops)
    return True

# Handles calculations
def calculation(user_input,history,un_ops,bin_ops):
    try: # Exception handling for invalid input

        parts = user_input.split()

        # Unary operation
        if len(parts) == 2:
            result=unary_calc(parts,un_ops)
            

        # Binary operation
        elif len(parts) == 3:
            result=binary_calc(parts,bin_ops)

        else:
            raise ValueError("Input format should be: 5 + 3 OR sqrt 25")

        if isinstance(result,float) and result.is_integer():
            result=int(result)

        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        exp=f"[{timestamp}] {user_input} = {result}"

        history.append(exp)

        print(result)
    except ValueError as e:
        print(e)

# Unary Operator Calculation
def unary_calc(parts,un_ops):
    # perform single-operand operation (e.g., sqrt, abs)
    operator, value=parts
    try:
        value=float(value)
    except ValueError:
        raise ValueError("Unary operand must be a valid number")
    if value.is_integer():
        value=int(value)
    if operator=="fact" and not isinstance(value,int):
        raise ValueError("Factorial only works with integers")
    if operator in un_ops:
        return un_ops[operator](value)
    else:
        raise ValueError("Invalid unary operator")
    
# Binary Operator Calculation
def binary_calc(parts,bin_ops):
    # perform two-operand operation (e.g., +, -, *)
    left,operator,right=parts
    left,right=float(left),float(right)
    if left.is_integer():
        left=int(left)
    if right.is_integer():
        right=int(right)
    if operator in bin_ops:
        return bin_ops[operator](left,right)
    else:
        raise ValueError("Invalid binary operator")

# main function
history=[]
un_ops={"sqrt": math.sqrt,"abs": abs,"sin": math.sin,"cos": math.cos,"tan": math.tan,"fact": factorial}
bin_ops={'+':add, '-': subtract, '*': multiply, '/': divide,'//': floor_divide, '%':modulus, '^': power}
print("Enter 'menu' for details")
while True:
     user_input=input(">>>").strip()
     if not process_command(user_input,history,un_ops,bin_ops):
        break
print("Program Terminated")