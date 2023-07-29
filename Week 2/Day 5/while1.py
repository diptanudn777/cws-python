"""
Aask a start number from user
Aask a end number from user

start to end -> total
"""

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))
i = start
total = 0
while i <= end:
    total = total + i
    i = i + 1
print(total)
