"""
print even numbers
"""
a = [54, 65, 34, 43, 32, 56, 43]

# for i in range(0, len(a)):
#     if a[i] % 2 == 0:
#         pass
#     else:
#         print(a[i])

for i in range(0, len(a)):
    if a[i] % 2 != 0:
        print(a[i])
