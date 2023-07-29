"""
Ask a number from user

Print positive, negative, equal to zero
"""

x = int(input("Enter a number: "))

if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Equals to 0")
