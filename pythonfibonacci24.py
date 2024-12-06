'''
Author : Aiwin Soji
Date : 06-12-2024
Aim :Program to define a module to find Fibonacci Numbers and import the module to another program.
'''

def fibonacci(num):
    list1=[]
    num1=0
    num2=1
    for i in range (num):
        list1.append(num1)
        num1,num2=num2,num1+num2
    return list1

print(fibonacci(9))