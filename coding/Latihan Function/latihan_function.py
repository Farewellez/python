import os
from functools import reduce

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# --------------------------Code Bellow-------------------------- #
def function(a,b):
    if b == 0:
        return 1
    else:
        return a * function(a, b - 1)

Function = [] 
for _ in range(2):
    user = int(input("Input some integer:\n"))
    Function.append(user)

print(function(Function[0], Function[1]))
# --------------------------------------------------------------- #
input("ENTER")
clear()