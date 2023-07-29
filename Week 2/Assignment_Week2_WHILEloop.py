# 1...
# start = int(input("Enter start number = "))
# end = int(input("Enter end number = "))

# i = start
# while i <= end:
#     print(i, end=" ")
#     i = i + 1

# 2...
# start = int(input("Enter start number = "))
# end = int(input("Enter end number = "))

# i = start
# while i <= end:
#     if i % 5 == 0 and i % 7 == 0:
#         print(i, end=" ")
#     i += 1

# 3...
# start = int(input("Enter start number = "))
# end = int(input("Enter end number = "))

# i = start
# total = 0
# while i <= end:
#     if i % 4 == 0:
#         total = total + i
#     i += 1
# print(total)

# 4...
# i = 1
# prod = 1
# while i <= 10:
#     prod = prod * i
#     i += 1
# print(prod)

# 5...
# num = int(input("Enter a number = "))
# i = 1
# while i <= 10:
#     print(num, "X", i, "=", num * i)
#     i += 1

# 6...
# i = 20
# count = 0
# while i <= 70:
#     if i % 4 == 0:
#         count = count + 1
#     i += 1
# print(count)

# 7...
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
