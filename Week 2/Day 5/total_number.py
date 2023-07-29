"""
1 to 10.. totl print
1+2+3+4+5+6+7+8+9+10

Ask a number from user
1 to n.. total of all numbers
"""

# i = 1
# total = 0
# while i <= 10:
#     total = total + i
#     i = i + 1
# print(total)

n = int(input("Enter end number = "))
i = 1
total = 0
while i <= n:
    total = total + i
    i = i + 1
print(total)
