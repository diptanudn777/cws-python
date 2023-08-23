"""
Write a function prodDigits() that inputs a number and prints the product of digits of that number.
"""


def prodDigits():
    num = int(input("Enter a number = "))
    total = 1
    for i in str(num):
        total = total * int(i)
    print(total)


prodDigits()
prodDigits()
