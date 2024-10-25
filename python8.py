"""Author= Aiwin soji
Date= 25-10-2024
AIM: Write a Python program to find the largest of three numbers. The program should take three numbers as input from the user and determine which one is the largest.
Use conditional statements to compare the numbers."""

num1=int(input("Enter the first number"))
num2=int(input("Enter the second numbers"))
if num1>num2:
    print(num1,"is greater than",num2)
else:
    print(num2,"is greater than",num1)

if num1>0:
    print(num1,"is positive")
else:
    print(num1,"is negative")
if num2 > 0:
    print(num2, "is positive")
else:
    print(num2, "is negative")