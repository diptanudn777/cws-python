"""
Make a function which adds 2 functions using parameter
Make a function to check if the number is add or even
"""


def add(a: int, b: int):
    total = a + b
    return total


def check(n: int):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


r = add(3, 4)
check(r)
