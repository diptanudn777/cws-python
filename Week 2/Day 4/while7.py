"""
Ask a number from user

Print 1 to number, which are divisible by 5
"""
n = int(input("Enter a number= "))
i = 1
while i <= n:
    if i % 5 == 0:
        print(i, end=" ")
    i += 1

# n = int(input("Enter a number from user = "))
# i = 1
# while 1 <= n:
#     print(i, end=" ")
#     i = i + 1
