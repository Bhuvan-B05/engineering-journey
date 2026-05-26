from datetime import datetime
from history_manager import save_history, load_history, clear_history
from ui import menu

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