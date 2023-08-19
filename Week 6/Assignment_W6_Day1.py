# #Q1. Write a Python program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# # Sample Dictionary ( n = 5) :
# # Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# # Ask n from user.
# -----------------------
# n = int(input("Please enter the value of n: "))
# d = dict()
# for i in range(1, n + 1):
#     d[i] = i * i
# print(d)

# #Q2. Write a Python program to check if a dictionary is empty or not.
# d = {}
# if not d:
#     print("The dictionary is empty.")
# else:
#     print("The dictionary is not empty.")

# #Q3. Write a Python program to combine two dictionary by adding values for common keys.
# # d1 = {'a': 100, 'b': 200, 'c':300}
# # d2 = {'a': 300, 'b': 200, 'd':400}
# # Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
# --------------------------
# d1 = {"a": 100, "b": 200, "c": 300}
# d2 = {"a": 300, "b": 200, "d": 400}

# result = {}

# for i in d1:
#     if i in d2:
#         result[i] = d1[i] + d2[i]
#     else:
#         result[i] = d1[i]

# # for key in d2: # if d2 uncommon value required
# #     if key not in d1:
# #         result[key] = d2[key]

# print(result)

# #Q4. Python program to find the size of a Dictionary. Basically print how many total key-value pair are there.
# d = {"a": 1, "b": 2, "c": 3}
# size = len(d)
# print(f"The number of total key-value pair are: {size}")

# #Q5. Write a Python program to remove duplicates from Dictionary.
# # Sample dictionary: dictionary = {1: 60, 2: 50, 3: 40, 4: 30, 5: 20, 6: 10, 7:60, 8:50}
# # Output: {1: 60, 2: 50, 3: 40, 4: 30, 5: 20, 6: 10}
# ------------------------
# dictionary = {1: 60, 2: 50, 3: 40, 4: 30, 5: 20, 6: 10, 7: 60, 8: 50}
# a = {}

# for i in dictionary:
#     if dictionary[i] not in a.values():
#         a[i] = dictionary[i]
# print(a)

# -------------------------------

# a = {1: 60, 2: 50, 3: 40, 4: 30, 5: 20, 6: 10, 7: 60, 8: 50}
# b = {}

# for k, v in a.items():
#     if v not in b.values():
#         b[k] = v

# print(b)

n, x, y = map(int, input("").split())
n = n - x
a = n - y
print(n, a)
