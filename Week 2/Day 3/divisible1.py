"""
a= enter number 1 =
b= enter number 2 =

If a is divisible by b then print yes or print no
"""

a = int(input("Enter number 1 = "))
b = int(input("Enter number 2 = "))

if a % b == 0:
    print("Yes")
else:
    print("No")
