# #Q1. Reverse the order of words in a sentence. For example, change "Hello World" to "World Hello".

# # Example 1:
# # Input: "Hello World"
# # Output: "World Hello"
# #
# # Example 2:
# # Input: "Coding is fun"
# # Output: "fun is Coding"
# #
# # Example 3:
# # Input: "Python programming"
# # Output: "programming Python"

# a = "Coding is fun"

# a = a.split(" ")

# a.reverse()

# a = " ".join(a)
# print(a)
# ----------------------------------------------------------------

# #Q2. Given a list of strings, concatenate them into a single string separated by spaces. For example, given the input ["Hello", "World", "Python"], the output should be "Hello World Python".

# # Make a list on your own.
# # Don’t use the JOIN function.

# # Make a list of strings on your own
# my_list = ["Hello", "World", "Python"]

# # Initialize an empty string to store the result
# result = ""

# # Loop through each string in the list
# for string in my_list:
#     # Add the string and a space to the result
#     result += string + " "

# # Remove the extra space at the end of the result
# result = result[:-1]

# # Print the result
# print(result)  # I love Python

# -------------------------------------------------------
# a = ["Hello", "World", "Python"]


# out = ""
# for i in a:
#     out += i + " "
# out = out[:-1]  # to remove the extra space at the end
# print(out)
# ------------------------------------------------------------------------

# #Q3. Write a program to rotate the characters in a string by a given number of positions. For example, given the input "abcdef" and rotation of 2, the output should be "efabcd".

# # Ask string and rotation from the user.

# # Ask string and rotation from the user
# string = input("Enter a string: ")
# rotation = int(input("Enter a rotation: "))

# # Calculate the length of the string
# length = len(string)

# # Adjust the rotation to be within the range of the length
# rotation = rotation % length

# # Split the string into two parts: the left part and the right part
# left_part = string[:length - rotation]
# right_part = string[length - rotation:]

# # Concatenate the right part and the left part to get the rotated string
# rotated_string = right_part + left_part

# # Print the rotated string
# print(rotated_string)

# ------------------------------------------------------
# a = input("Enter a string: ")
# r = int(input("Enter a rotation: "))

# l = len(a)

# r = r % l

# left_part = a[: l - r]
# right_part = a[l - r :]

# rotated_a = right_part + left_part
# print(rotated_a)
# ---------------------------------------------------------------------------

# #Q4. Given two strings s1 and s2. The task is to find out the minimum number of string rotations for the given string s1 to obtain the actual string s2.

# # Example 1
# # Input:
# # s1 = "abcd"
# # s2 = "cdab"
# #
# # Output:
# # 2
# #
# # Example 2
# # Input:
# # s1 = "hello"
# # s2 = "lohel"
# #
# # Output:
# # 2
# #
# # Example 3
# # Input:
# # s1 = "programming"
# # s2 = "mingprogram"
# #
# # Output:
# # 4
# #
# # Example 4
# # Input:
# # s1 = "abcdef"
# # s2 = "defabc"
# #
# # Output:
# # 3
# ---------------------

# # Given two strings s1 and s2
# s1 = "programming"
# s2 = "mingprogram"

# # Initialize a variable to store the number of rotations
# rotations = 0

# # Check if the strings have the same length
# if len(s1) == len(s2):
#     # Loop until s1 is equal to s2 or the number of rotations exceeds the length of s1
#     while s1 != s2 and rotations < len(s1):
#         # Rotate s1 by one position to the right
#         s1 = s1[-1] + s1[:-1]
#         # Increment the number of rotations by one
#         rotations += 1
#     # If s1 is equal to s2, print the number of rotations
#     if s1 == s2:
#         print(rotations)
#     # Else, print -1 to indicate that s2 cannot be obtained from s1 by any number of rotations
#     else:
#         print(-1)
# # Else, print -1 to indicate that s2 cannot be obtained from s1 by any number of rotations
# else:
#     print(-1)
# ----------------------------------------

# s1 = "programming"
# s2 = "mingprogram"

# rotations = 0

# if len(s1) == len(s2):
#     while s1 != s2 and rotations < len(s1):
#         s1 = s1[-1] + s1[:-1]
#         rotations += 1
#     if s1 == s2:
#         print(rotations)
#     else:
#         print("Can't be obtained")

# else:
#     print("Can't be obtained")
# -------------------------------------------------------------------------

# #Q5. Write a Python program to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

# # Input: pyTHon
# # Output: PYTHON
# #
# # Input: helLo
# # Output: helLo
# #
# # Input: gOOD
# # Output: GOOD
# --------------------------

# # Given a string
# string = "pyTHon"

# # Initialize a variable to count the number of uppercase characters in the first 4 characters
# upper_count = 0

# # Loop through the first 4 characters of the string
# for char in string[:4]:
#     # If the character is uppercase, increment the upper_count by one
#     if char.isupper():
#         upper_count += 1

# # If the upper_count is at least 2, convert the string to all uppercase
# if upper_count >= 2:
#     string = string.upper()

# # Print the string
# print(string)
# -----------------------------

a = "pyTHon"
upper_count = 0

for i in a[:4]:
    if i.isupper():
        upper_count += 1
if upper_count >= 2:
    a = a.upper()
print(a)
