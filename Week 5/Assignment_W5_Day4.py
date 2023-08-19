# #Q1. Write a Python program to check if a string is empty or not.
# s = input("Please enter a string: ")
# print(s)
# if not s:
#     print("The string is empty.")
# else:
#     print("The string is not empty.")

# #Q2. Write a Python program to find the length of the longest word in a string.
# #Example 1:
# #Input: "The quick brown fox jumps over the lazy dog."
# #Output: Length of the longest word: 5
# #Example 2:
# #Input: "I love coding in Python!"
# #Output: Length of the longest word: 6
# #Example 3:
# #Input: "Hello, World!"
# #Output: Length of the longest word: 5

# a = "hello good morning"

# words = a.split()
# print(words)

# largest_length = 0
# largest_word = ""

# for w in words:
#     if len(w) > largest_length:
#         largest_length = len(w)
#         largest_word = w

# print(largest_length)
# print(largest_word)

# #Q3. Write a Python program to find the most common character in a string. (Print the letter which repeats most of the time)
# # Example 1:
# # Input: "hello"
# # Output: Most common character: l
# # Example 2:
# # Input: "programming"
# # Output: Most common character: g
# # Example 3:
# # Input: "mississippi"
# # Output: Most common character: i
# # Q4. Write a Python program to remove duplicate characters from a string and return the modified string.
# # Example 1:
# # Input: "hello"
# # Output: Modified string: helo
# # Example 2:
# # Input: "programming"
# # Output: Modified string: progamin
# # Example 3:
# # Input: "mississippi"
# # Output: Modified string: misp

# s = "programming"

# freq = {}  # create an empty dictionary

# for c in s:  # iterate over the string
#     if c in freq:  # if character is in dictionary, increment its value
#         freq[c] += 1  # else, assign it to 1
#     else:
#         freq[c] = 1

# max_value = max(freq.values())  # find the maximum value in the dictionary

# max_keys = [
#     k for k, v in freq.items() if v == max_value
# ]  # find the keys that have the maximum value

# print(
#     "Most common character(s):", ", ".join(max_keys))  # print the most common character(s)

# #Q4. Write a Python program to remove duplicate characters from a string and return the modified string.
# # Example 1:
# # Input: "hello"
# # Output: Modified string: helo
# # Example 2:
# # Input: "programming"
# # Output: Modified string: progamin
# # Example 3:
# # Input: "mississippi"
# # Output: Modified string: misp

# input string
# s = "mississippi"

# # create an empty string
# unique = ""

# # iterate over the string
# for c in s:
#   # check if the character is already in the unique string
#   if c not in unique:
#     # append the character to the unique string
#     unique += c

# # assign the unique string to the modified variable
# modified = unique

# # print the modified string
# print("Modified string:", modified)

# #Q5. Write a Python program to check if a string is an isogram (no repeating characters).
# # Example 1:
# # Input: "algorithm"
# # Output: No, the string is not an isogram.
# # Example 2:
# # Input: "python"
# # Output: Yes, the string is an isogram.
# # Example 3:
# # Input: "hello"
# # Output: No, the string is not an isogram.
# # Example 4:
# # Input: "racecar"
# # Output: No, the string is not an isogram.
# # Example 5:
# # Input: "book"
# # Output: Yes, the string is an isogram.

# input string
# s = "algorithm"

# # convert the string to lowercase and create a set of characters
# unique = set(s.lower())

# # check if the length of the set is equal to the length of the string
# if len(unique) == len(s):
#   # print that the string is an isogram
#   print("Yes, the string is an isogram.")
# else:
#   # print that the string is not an isogram
#   print("No, the string is not an isogram.")

# #Q6. Write a Python program to find the most frequent word in a string.
# #Example 1:
# #Input: "The quick brown fox jumps over the lazy dog."
# #Output: Most frequent word: the
# #Example 2:
# #Input: "She sells seashells by the seashore."
# #Output: Most frequent word: seashells
# #Example 3:
# #Input: "To be or not to be, that is the question."
# #Output: Most frequent word: to
# #Example 4:
# #Input: "I scream, you scream, we all scream for ice cream!"
# #Output: Most frequent word: scream
# #Example 5:
# #Input: "The cat in the hat."
# #Output: Most frequent word: the

# # input string
# s = "She sells seashells by the seashore."

# # create an empty dictionary
# word_count = {}

# # split the string into words and iterate over them
# for word in s.split():
#   # convert the word to lowercase and strip any punctuation
#   word = word.lower().strip(".,")

#   # check if the word is already in the dictionary
#   if word in word_count:
#     # increment the count by one
#     word_count[word] += 1
#   else:
#     # initialize the count to one
#     word_count[word] = 1

# # create a variable to store the most frequent word and its count
# most_frequent = ("", 0)

# # loop through the dictionary items
# for key, value in word_count.items():
#   # check if the value is greater than the current maximum
#   if value > most_frequent[1]:
#     # update the most frequent word and its count
#     most_frequent = (key, value)

# # print the most frequent word
# print("Most frequent word:", most_frequent[0])
