# def primeNumber():
#     num = int(input("Enter a number: "))

#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 print(num, "is not a prime number")
#                 break
#         else:
#             print(num, "is a prime number")
#     else:
#         print(num, "is not a prime number")


# primeNumber()
# -------------------------


def primeNumber():
    num = int(input("Enter a number: "))  # 7
    count = 0
    for i in range(1, num + 1):  # 1 to 7 (i)
        if num % i == 0:
            count += 1
    if count == 2:
        print("Prime Number!")
    else:
        print("Not a Prime Number!")


primeNumber()
