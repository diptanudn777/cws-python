# #Q1. Make your own list of numbers. Ask a start and end position from User. Print the list from start position to end position using Slicing.
# a = [54, 2, 1, 43, 676, 45, 45, 45, 21, 787, 45]
# s = int(input("Enter start pos = "))
# e = int(input("Enter end pos = "))

# b = a[s:e+1]
# print(b)

# #Q2. Make your own list of numbers. Ask a start and end position from User. Make another different list which will contain number from start to end position. Use slicing logic.
# my_list = [10, -5, 8, 3, -1, -9, 7, 2]
# s = int(input("Enter start pos = "))
# e = int(input("Enter end pos = "))

# b = my_list[s : e + 1]
# print(b)

# #Q3. Make your own list. Write a Python program that takes an integer as an input, and make a new list containing the last n elements of the original list. Using slicing logic.
# my_list = [10, -5, 8, 3, -1, -9, 7, 2]
# n = int(input("Enter end pos starting from last = "))

# b = my_list[len(my_list) - n :]
# print(b)

# #Q4. Make your own list. Write a Python program that takes an integer as an input, and make a new list containing the last n elements of the original list but in reverse order. Using slicing logic.
# my_list = [10, -5, 8, 3, -1, -9, 7, 2]
# n = int(input("Enter end pos starting from last = "))

# b = my_list[-1 : n - 1 : -1]
# print(b)

# #Q5. Write a python program to interchange first and last elements in a list.
# my_list = [10, -5, 8, 3, -1, -9, 7, 2]
# print(f"The original list is {my_list}")
# first = my_list[-1]
# last = my_list[0]

# my_list[0] = first
# my_list[-1] = last
# print(f"The modified list is {my_list}")

# #Q6. Write a Python code to split a list into two halves using list slicing. (Keep the length of list even)
my_list = [10, -5, 8, 3, -1, -9, 7, 2]
print(f"The original list is {my_list}")

middle = len(my_list) // 2

first_half = my_list[:middle]
second_half = my_list[middle:]
print(f"The First Half is {first_half}")
print(f"The Second Half is {second_half}")
