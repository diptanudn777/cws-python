"""
sk a number from user

If a number is divisible by 2 & 3->Yes
Else -> No

Less then 1 -> Invalid
"""

num = int(input("Enter a number = "))

if num % 2 == 0 and num % 3 == 0:
    print("Yes")
elif num < 1:
    print("Invalid")
else:
    print("No")
