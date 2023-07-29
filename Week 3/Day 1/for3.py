"""
10 to 1
"""
# for i in range(10, 0, -1):
#     print(i, end=" ")


"""
enter number 1=
enter number 2=

3 to 10 (print increasing)

30 to 10 (print decreasing)
"""
a = int(input("Enter number 1 = "))
b = int(input("Enter number 2 = "))
if a < b:
    for i in range(a, b + 1):
        print(i, end=" ")
else:
    for i in range(a, b - 1, -1):
        print(i, end=" ")
