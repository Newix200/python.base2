'''
Author : Aiwin Soji
Date : 06-12-2024
Aim :Program to define a module to find Fibonacci Numbers and import the module to another program.
'''

def fibonacci(n):
    if n<0:
        print("Incorrect number")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-1)
    print(fibonacci(9))
