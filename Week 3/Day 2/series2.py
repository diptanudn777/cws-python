"""
1 2 4 7 11 16 22 29 37 ...upto 20 numbers
pttern: +1, +2, +3, +4
"""
number = 1
for i in range(1, 21):
    print(number, end=" ")
    number = number + i
