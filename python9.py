num1=int(input("Enter the first number"))
num2=int(input("Enter the second numbers"))
num3=int(input("Enter the third numbers"))

if num1>num2 and num1>num3:
    print(num1,"is greater")
elif num2>num3 and num2>num1:
    print(num2,"is greater")
else:
    print(num3,"is greater")