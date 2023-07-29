# def checkeven(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False


# # checkeven(5)

## FILTER FUNCTION:

# l = [4, 8, 9, 5, 10, 12, 16, 17]

# l1 = list(filter(checkeven, l))
# print(l1)

"""----------------------"""

## MaAP FUNCTION:

# def double(x):
#     result = 2 * x
#     return result

# l = [4, 6, 7, 8, 3, 5, 12, 16, 17]
# l2 = list(map(double, l))
# print(l2)


##REDUCE FUNCTION:

# from functools import *

# result = reduce(lambda x, y: x + y, range(1, 101))
# print(result)
