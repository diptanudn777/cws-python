"""
20

1,2,4,5,10,20
Total factors = 6
"""

# num = int(input("Enter a number = "))
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i, end=" ")

num = int(input("Enter a number = "))
count = 1
for i in range(1, num + 1):
    if num % i == 0:
        count = count + 1
    i += 1
print(count)

num = int(input("Enter a number = "))
i = 1
count = 0
while i <= num:
    if num % i == 0:
        count += 1
    i += 1
if count == 2:
    print("It's a prime number.")
else:
    print("It's not a prime number.")
