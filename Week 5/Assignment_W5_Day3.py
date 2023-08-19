# #Q1. Write a Python program to get the 4th element from the last element of a tuple.

# a = (1, 2, 3, 4, 5)
# print(a[3])

# #Q2. Write a Python program to find repeated items in a tuple.
# a = 2, 4, 5, 6, 2, 3, 4, 4, 7
# print(a)

# repeated = []
# for i in a:
#     if a.count(i) > 1 and i not in repeated:
#         repeated.append(i)
# print(repeated)

# #Q3. Write a Python program to check whether an element exists within a tuple.
# a = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
# print(a)

# element = "r"
# if element in a:
#     print(element, "is in the tuple")
# else:
#     print(element, "is not in the tuple")

# #Q4. Write a Python program to remove an item from a tuple.
# a = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
# print(a)

# item = "r"
# new_a = tuple(x for x in a if x != item)
# print(new_a)

# #Q5. Write a Python program to reverse a tuple.
# a = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
# print(a)

# a = a[::-1]
# print(a)

# #Q6. Write a Python program to check if a string has at least one letter and one number. If it has at least one letter and one number then print YES else print NO.
# s = "Hello123"
# print(s)

# has_letter = False
# has_number = False

# for c in s:
#     if c.isalpha():
#         has_letter = True
#     if c.isdigit():
#         has_number = True

# if has_letter and has_number:
#     print("YES")
# else:
#     print("NO")

# #Q7. Write a python program to ask a string from user. Then count the number of vowels and number of consonants in that string.
# s = input("Please enter a string: ")
# print(s)

# vowels = 0
# consonants = 0

# s = s.lower()

# for c in s:
#     if c in "aeiou":
#         vowels += 1
#     else:
#         consonants += 1

# print("Number of vowels:", vowels)
# print("Number of consonants:", consonants)

# #Q8. Ask a string from user. Print the string with first 2 letters and last 2 letters.
# #Example string: aeroplane
# #Output: aene
# s = input("Please enter a string: ")
# print(s)
# print(s[:2] + s[-2:])

# #Q9. Write a python program to only print the second half of the string. Ask string from user.
# #Example string: aeroplane
# #Output: lane
# #Example string: delhi
# #Output: hi
# #Example string: pavbhaji
# #Output: haji

s = input("Please enter a string: ")
print(s)
print(s[-(len(s) // 2) :])
