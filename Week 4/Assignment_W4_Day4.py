# #1. Write code that takes a list of numbers as input and calculates the sum of all the elements in the list. Remember first take input, and then calculate the sum without using sum() function.

# numbers = []
# n = int(input("How many numbers do you want to enter? "))
# for i in range(n):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)
# total = 0
# for number in numbers:
#     total += number
# print(f"The sum of the numbers is {total}")


# #2. Write code that takes a list as input, removes all duplicate elements from it.
# a = [54, 2, 1, 43, 676, 45, 54, 21, 1787, 2, 45]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)


# #3. Write code that takes two lists and prints the elements that are common to both lists.

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# c = []
# for i in list1:
#     if i in list2:
#         c.append(i)
# print(c)

# #4.  Write code that takes a list of numbers as input and prints a new list with the squares of each element.
# list1 = [1, 2, 3, 4, 5]
# s = []
# for i in list1:
#     s2 = i**2
#     s.append(s2)
# print(s)

# #5. Write code that checks if a given list is a palindrome, i.e., it reads the same backward as forward. Print "Palindrome" if it is, otherwise print "Not a Palindrome".
# list1 = [1, 2, 3, 2, 1]
# list2 = list1[::-1]

# if list1 == list2:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# #6. Write code that takes a list of elements as input and prints the count of each unique element along with the element itself.
# numbers = []
# n = int(input("How many numbers do you want to enter? "))
# for i in range(n):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)
# print(f"The count is = {len(numbers)} and the elements are = {numbers}")

# #7. Write code that takes a list of numbers and an integer 'n' as input. Print the index of the first occurrence of 'n' in the list, or print "Not found" if 'n' is not present.

a = [54, 2, 1, 43, 676, 45, 45, 45, 21, 787, 45]
num = int(input("Enter a number = "))
if a.count(num) > 0:
    for i in range(0, len(a)):
        if a[i] == num:
            print(f"{num} is at position = {i}")
            break
else:
    print("Not found")

# #8. Write code that takes a list of numbers as input and calculates the sum of elements at even indices and the sum of elements at odd indices separately. Print both sums.
# n = int(input("How many numbers do you want to enter? "))
# numbers = []
# for i in range(n):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)
# even_sum = 0
# odd_sum = 0
# for i in range(len(numbers)):
#     if i % 2 == 0:
#         even_sum += numbers[i]
#     else:
#         odd_sum += numbers[i]
# print(f"The sum of elements at even indices is {even_sum}")
# print(f"The sum of elements at odd indices is {odd_sum}")
