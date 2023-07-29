# 1.a...
# start = 10
# end = 200

# i = start
# while i <= end:
#     print(i, end=" ")
#     i = i + 10

# 1.b...
# start = 1
# end = 100000000

# i = start
# while i <= end:
#     print(i, end=" ")
#     i = i * 10

# 1.c...
# start = 1

# i = start
# while i <= 10:
#     print(i * "1", end=" ")
#     i = i + 1

####... 1.d... (1 3 6 8 11 13 16 … 28)

i = 1
counter = 2
while i <= 28:
    print(i, end=" ")
    i = i + counter
    if counter == 2:
        counter = 3
    else:
        counter = 2


# 1.e...
# i = 1
# while i <= 2048:
#     print(i, end=" ")
#     i = i * 2


# 2...
# n = int(input("Enter a number = "))
# sum = 0
# i = 0

# while i <= n:
#     sum = sum + 1 / (2**i)
#     i = i + 1

# print(f"The sum of the series is = {sum}")

# 3...
# i = 1
# sum = 0

# while i <= 10:
#     sum = sum + i**2
#     i = i + 1

# print(sum)


# 4...
# i = 1
# while i <= 100:
#     if i % 2 == 0 and i % 3 == 0 and i % 8 != 0:
#         print(i, end=" ")
#     i = i + 1
