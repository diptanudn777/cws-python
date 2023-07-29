"""
1 2 4 8 16 32 64 ... upto 15 numbers
"""

# for i in range(1, 16):
#     print(2**i, end=" ")

number = 1
for i in range(1, 16):
    print(number, end=" ")
    number = number * 2
