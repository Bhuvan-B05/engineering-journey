from parser import process_command
from operations import un_ops, bin_ops
# main function
history=[]
print("Enter 'menu' for details")
while True:
     user_input=input(">>>").strip()
     if not process_command(user_input,history,un_ops,bin_ops):
        break
print("Program Terminated")