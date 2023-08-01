# Q1. Make a list. Print the length of that list.
# a = [23, 54, 65, 32, 23, 54, 65, 7]
# print(len(a))

# Q2. Make a list. Tell if the length of that list is Even or Odd.
# a = [23, 54, 65, 32, 23, 54, 65, 7]
# # x = len(a)
# if len(a) % 2 == 0:
#     list = "even"
# else:
#     list = "odd"
# print(f"The length of the list is = {list}")

# Q3. Make a list. Find the sum of all the elements in list which are divisible by 3.
# a = [23, 54, 65, 32, 23, 54, 65, 7, 9]
# sum = 0
# for i in a:
#     if i % 3 == 0:
#         sum = sum + i
# print(sum)

# Q4. Make a list. Find how many positive and negative numbers are there.
# a = [23, -54, 65, -32, -23, 54, 65, 7, 9, -2]
# count = 0
# count2 = 0
# for i in a:
#     if i >= 0:
#         count = count + 1
#     else:
#         count2 = count2 + 1
# print(f"Total positive numbers = {count} and negative numbers = {count2}")

# Q5. Make a list. Print all the elements in a list in reverse order.
# a = [23, -54, 65, -32, -23, 54, 65, 7, 9, -2]
# a.reverse()
# print(a)

# print(a[::-1])

# a = [23, -54, 65, -32, -23, 54, 65, 7, 9, -2]
# for i in range(len(a) - 1, -1, -1):
#     print(a[i], end=" ")


# Q6. Make a list. Now print all the elements based on even index/position.
# Example:
# my_list=[45, 12, 59, 60, 47, 3412, 3111]
# Output:
# 45 59 47 3111
# a = [45, 12, 59, 60, 47, 3412, 3111]
# for i in a:
#     if i % 2 != 0:
#         print(i, end=" ")

# a = [45, 12, 59, 60, 47, 3412, 3111]
# for i in range(0, len(a), 2):
#     print(a[i], end=" ")


a = [45, 12, 59, 60, 47, 3412, 3111]
for i in range(0, len(a), 2):
    print(a[i], end=" ")
