"""
1 11 101 1001 10001 100001 1000001 ... upto 10 numbers
"""
number = 1
for i in range(1, 11):
    print(number, end=" ")
    number = (10**i) + 1
