"""
1 to 20

Divisible by 3...Count
"""

# for i in range(1, 21):
#     if i % 3 == 0:
#         print(i)


i = 1
count = 0
while i <= 20:
    if i % 3 == 0:
        count = count + 1
    i = i + 1
print(count)
