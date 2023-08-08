# #Q1. Make your own list, find the largest element from that list without using the sort() method.

# numbers = []
# n = int(input("How many numbers do you want to enter? "))
# for i in range(n):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)
# print(f"The elements are = {numbers}")

# a = numbers
# largest = a[0]
# for i in range(0, len(a)):
#     if a[i] > largest:
#         largest = a[i]
# print(f"The largest element is = {largest}")


# #Q2. Make your own list. Ask a frequency from the user. Print only those numbers in that list which have count greater than or equal to the frequency entered by the user.
# mylist = [54, 2, 2, 31, 223, 54, 54, 76, 2, 21, 43, 54, 5, 12]
# unique_elements = []

# freq = int(input("Enter frequency = "))

# for i in mylist:
#     if i not in unique_elements:
#         unique_elements.append(i)
# # #print(unique_elements)

# for i in unique_elements:
#     if mylist.count(i) >= freq:
#         print(i, end=" ")


# #Q3. Make your own list, calculate the product of all the numbers excluding the duplicates.
# mylist = [1, 4, 6, 7, 7]
# total = 0
# for i in mylist:
#     if mylist.count(i) == 1:
#         if total == 0:
#             total = 1
#         total = total * i
# print(total)

##------------------------------------------
# #a = [1, 4, 6, 7, 7]
# a = []
# n = int(input("How many numbers do you want to enter? "))
# for i in range(n):
#     num = int(input(f"Enter number {i+1}: "))
#     a.append(num)
# print(f"The elements are = {a}")

# count_dict = {}
# for i in a:
#     if i in count_dict:
#         count_dict[i] += 1
#     else:
#         count_dict[i] = 1

# b = []
# for key, value in count_dict.items():
#     if value == 1:
#         b.append(key)
# print(f"New list = {b}")

# prod = 1
# for i in b:
#     prod = prod * i
# print(prod)
##--------------------------------------------

# #Q4. Find the missing number from the list, the numbers missing from the list should only be printed. Make sure the list you take is always sorted.
# mylist = [3, 4, 6, 7, 8]

# start_number = mylist[0]
# end_number = mylist[-1]
# missing_numbers = []

# for i in range(start_number, end_number + 1):
#     if i not in mylist:
#         missing_numbers.append(i)

# print(f"Missing numbers = {missing_numbers}")

# #Q5. Make your own list. Ask a rotation number from the user. Rotate the list by the amount of number entered by the user.
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# rotation = int(input("Enter rotation = "))
# for i in range(rotation):
#     # Add last element to start of the list
#     mylist.insert(0, mylist[-1])

#     # Delete the last element
#     mylist.pop()
# print(mylist)
##-------------------------------
# #a = [1, 4, 6, 7, 7]
# a = []
# n = int(input("How many numbers do you want to enter? "))
# for i in range(n):
#     num = int(input(f"Enter number {i+1}: "))
#     a.append(num)
# print(f"The elements are = {a}")

# num = int(input("Enter rotation = "))
# b = a[len(a) - num : len(a)]
# # #print(b)

# for i in a[0 : len(a) - num]:
#     b.append(i)
# print(f"New list after rotation = {b}")
##---------------------------------
