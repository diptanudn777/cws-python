"""
Ask 5 numbers from user,
count how many are even
"""
a = []

for _ in range(1, 6):
    num = int(input("Enter a number = "))
    a.append(num)

count = 0
for i in a:
    if i % 2 == 0:
        count += 1
print(count)
