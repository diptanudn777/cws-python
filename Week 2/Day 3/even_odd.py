"""
Ask number from user, prnt is it odd or even or equal to zero
"""

number = int(input("Enter a number = "))

if number % 2 == 0:
    print("Even")
elif number % 2 != 0:  # number%2==1:
    print("Odd")
else:
    ("Equal to zero")
