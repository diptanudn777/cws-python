"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(i, end=" ")
#     print()

# -------------------
"""
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
