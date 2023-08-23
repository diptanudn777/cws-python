"""
Make a function, which accepts 1 list as a parameter, return sum

Make a function to check if a number is prime or not
"""


# def printList(a):
#     print(a)


# my_list = [3, 4, 5, 6]
# printList(my_list)
# --------------------------


def returnListSum(a):
    return sum(a)


def checkPrime(n):
    factors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factors += 1
    if factors == 2:
        print("Prime")
    else:
        print("Not Prime")


my_list = [1, 2, 3, 4]
result = returnListSum(my_list)
print(result)
checkPrime(result)
