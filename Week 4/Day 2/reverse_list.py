"""
length=5
Position=0 to 4

Reverse print= 4 to 0
"""

a = [43, 21, 45, 65, 67]

for i in range(len(a) - 1, -1, -1):
    print(a[i], end=" ")
