'''
Author : Aiwin Soji
Date : 06-12-2024
Aim :Program to define a module to find Fibonacci Numbers and import the module to another program.
'''
def fibonacci(n):
    num1=0
    num2=1
    new_number=num2
    count=1
    while count<=n-1:
        print(new_number,end=" ")
        count+=1
        num1, num2= num2, new_number
        new_number =num1+num2
    print()
fibonacci(9)
