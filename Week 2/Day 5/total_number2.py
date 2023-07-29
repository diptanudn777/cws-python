"""
1 to 100

Divisible 6-> Total
"""

i = 1
total = 0
while i <= 100:
    if i % 6 == 0:
        total = total + i
    i = i + 1
print(total)
