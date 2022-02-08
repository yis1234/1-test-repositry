"""Biggest number
Check which number is larger
Sun Woo Yi
04/02/22
"""
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
if number1 < number2:
    print("The second number is larger than the first number")
elif number1 > number2:
    print("The first number is larger than the second number")
else:
    print("The first number and the second number are equal")
