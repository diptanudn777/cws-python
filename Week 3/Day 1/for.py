"""
1 to 10
"""

# for i in range(1, 11):
#     print(i, end=" ")

# a=int(input("Enter a number = "))
# for i in range(1, a+1):
#     print(i, end=" ")

a = int(input("Enter start number = "))
b = int(input("Enter end number = "))
total = 0
for i in range(a, b + 1):
    total = total + i
print(total)
