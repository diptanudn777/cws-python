# # Assignment - Week 7 - Functions


# # Q1. Write a Python function is_palindrome(s) that takes a string s as input and returns True if the string is a palindrome (reads the same forwards and backwards), and False otherwise.
# -----------------------
# s = input("Enter a string: ")


# def is_palindrome(s):  # def is_palindrome(s: str) -> bool:
#     return s == s[::-1]


# print(is_palindrome(s))

# -----------------------
# s = input("Enter a string: ")
# n = len(s)
# is_palindrome = True
# for i in range(n // 2):
#     if s[i] != s[n - i - 1]:
#         is_palindrome = False
#         break
# if is_palindrome:
#     print(f"{s} is a palindrome.")
# else:
#     print(f"{s} is not a palindrome.")

# -------------------   ------------------------   -------------------------
# # Q2. Write a Python function factorial(n) that calculates and returns the factorial of a non-negative integer n.
# -----------------------
# n = int(input("Enter a non-negative integer: "))

# if n < 0:
#     print("Error: n must be non-negative.")
# else:
#     fact = 1
#     for i in range(1, n + 1):
#         fact = fact * i
#     print(f"The factorial of {n} is {fact}.")


# -------------------   ------------------------   -------------------------
# # Q3. Write a Python function word_count(sentence) that takes a sentence as input and returns a dictionary where keys are words and values are the counts of those words in the sentence.
# #
# # Examples
# # test_case_1 = "The quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dog"
# # test_case_2 = "Hello world This is a test Hello world"
# # test_case_3 = "Python Python python python programming Programming is FUN!"
# #
# # Outputs:
# # {'the': 4, 'quick': 2, 'brown': 2, 'fox': 2, 'jumps': 2, 'over': 2, 'lazy': 2, 'dog': 2}
# # {'hello': 2, 'world': 2, 'this': 1, 'is': 1, 'a': 1, 'test': 1}
# # {'python': 4, 'programming': 2, 'is': 1, 'fun': 1}
# #
# # These are just examples for better understanding.
# -----------------------
# sentence = input("Enter the sentence to count: ")


# def word_count(sentence): # def word_count(sentence: str) -> dict:
#     words = sentence.lower().split()
#     word_count = {}
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#     return word_count


# print(word_count(sentence))

# -------------------   ------------------------   -------------------------
# # Q4. Write a Python function flatten_list(nested_list) that takes a nested list as input and returns a flattened version of the list.
# # Examples:
# # nested_list_1 = [1, [2, 3, [4, 5]], 6, [7, 8]]
# # nested_list_2 = [1, [2, [3, [4, [5]]]]]
# # nested_list_3 = [1, 2, 3, 4, 5]
# #
# # Outputs:
# # [1, 2, 3, 4, 5, 6, 7, 8]
# # [1, 2, 3, 4, 5]
# # [1, 2, 3, 4, 5]
# -----------------------
nested_list = eval(input("Enter a nested list: "))


def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list


print(flatten_list(nested_list))
