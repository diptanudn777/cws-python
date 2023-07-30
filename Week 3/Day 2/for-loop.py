"""
Enter start number = 1
Enter end number = 100

Count of numbers divisible by- 5 and 6

3
"""

a = int(input("Enter start number = "))
b = int(input("Enter end number = "))
c = int(input("Enter end number = "))
count = 0

for i in range(a, b + 1):
    if i % 5 == 0 and i % 6 == 0:
        count = count + 1
print(f"Total number divisible by 5 and 6 is: {count}")
