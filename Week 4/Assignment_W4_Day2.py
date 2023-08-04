# #Q1. Write a Python program to check a list is empty or not.

# def check_list(a):
#     for i in a:
#         return False
#     return True

# a = []

# if check_list(a):
#     print("The list is empty")
# else:
#     print("The list is not empty")

# #Q3. Write a Python program to find the second smallest number in a list.
# a = [100, 211, 113, 4, 76, 73, 13]

# a.sort()
# print(a[1])


# #Q4. Write a Python program to find the second largest number in a list.
# a = [100, 211, 113, 4, 76, 73, 13]

# a.sort()
# print(a[-2])


# #Q6. Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.

# a = []
# b = []
# for _ in range(1, 11):
#     num = int(input("Enter a number = "))
#     a.append(num)
# for i in a:
#     b.append(i)
# b.reverse()
# print(b)

# #Q7. Write a program to find the average of all the numbers present in the list.
# a = [100, 211, 113, 4, 76, 73, 13]
# total = 0
# for i in a:
#     total = total + i
# print(round(total / len(a), 2))

# #Q8. Make 2 different list. First merge both list into third variable. And sort the merge list in descending order.

# a = [43, 45, 1, 1, 43, 54, 22]
# b = [65, 7, 87, 5, 343, 44]
# c = []

# for i in a:
#     c.append(i)
# for i in b:
#     c.append(i)
# c.sort(reverse=True)
# print(c)

# #Q9. Make a list. Write a simple program for addition of the 2 nd element from start and 2 nd element from the end.

a = [43, 45, 1, 1, 43, 54, 22, 65, 7, 87, 5, 343, 44]
sum = a[1] + a[-2]
print(sum)
