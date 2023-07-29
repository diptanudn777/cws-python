"""
Enter a number = 15

1 3 5 15

20
1 2 4 5 10
"""

# num = int(input("Enter a number = "))  # 15
# i = 1

# while i <= num:
#     if num % i == 0:
#         print(i, end=" ")
#     i = i + 1


# # Check for Prime numbers:...
num = int(input("Enter a number = "))  # 15
i = 1
count = 0
while i <= num:
    if num % i == 0:
        count = count + 1
    i = i + 1

if count == 2:
    print("It's a prime number")
else:
    print("It's not a prime number")
