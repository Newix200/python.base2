'''Author:Aiwin Soji
Date:P 18-10-2024:
Python program that uses functions from the math module
to perform the following operations on a number provided by the user:'''

import math
number=int(input("Enter a number:"))
square_root=math.sqrt(number)
print("square root of ",number,":",square_root)
factorial=math.factorial(number)
print("Factorial of ",number ,":",factorial)
power=math.pow(number,2)
print(number,"raised to 2:",power)