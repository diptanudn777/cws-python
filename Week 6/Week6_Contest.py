# # Q1. Create a dictionary that counts the frequency of words in a given string. Ask string from user.
# #
# # Example 1
# # Input String: "The sun is shining and the weather is nice"
# #
# # Output:
# # {
# #     'The': 1,
# #     'sun': 1,
# #     'is': 2,
# #     'shining': 1,
# #     'and': 1,
# #     'the': 1,
# #     'weather': 1,
# #     'nice': 1
# # }
# #
# # Example 2
# # Input String: “The cat and the dog played in the park The cat chased the dog”
# #
# # Output:
# # {
# #     'The': 2,
# #     'cat': 2,
# #     'and': 1,
# #     'dog': 2,
# #     'played': 1,
# #     'in': 1,
# #     'the': 3,
# #     'park': 1,
# #     'chased': 1
# # }

# --------------------------
# string = input("Enter a string: ")
# words = string.split()
# freq_dict = {}
# for i in words:
#     if i in freq_dict:
#         freq_dict[i] += 1
#     else:
#         freq_dict[i] = 1
# print(freq_dict)


# # --------------------------------------------------
# # Q2. Combine two dictionaries into a single dictionary, adding values for common keys.
# #
# # Dictionary 1
# # {
# #     'a': 10,
# #     'b': 20,
# #     'c': 30
# # }
# #
# # Dictionary 2
# # {
# #     'b': 5,
# #     'c': 15,
# #     'd': 25
# # }
# #
# # Output Dictionary
# # {
# #     'a': 10,
# #     'b': 25,  # Value added: 20 + 5
# #     'c': 45,  # Value added: 30 + 15
# #     'd': 25
# # }

# --------------------------
# dict1 = {"a": 10, "b": 20, "c": 30}
# dict2 = {"b": 5, "c": 15, "d": 25}

# for k in dict2:
#     if k in dict1:
#         dict1[k] += dict2[k]
#     else:
#         dict1[k] = dict2[k]

# print(dict1)

# # --------------------------------------------------
# # Q3. Write a Python program to map two lists into a dictionary. Everything in both lists should be unique.
# #
# # Example 1
# # list1 = ['red', 'green', 'blue']
# # list2 = ['#FF0000','#008000', '#0000FF']
# #
# # Output: {'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}
# #
# # Example 2
# # a = [“Anirudh”, ”Sanjay”, ”Sagar”]
# # b = [33, 66, 88]
# #
# # Output: {“Anirudh”:33, ”Sanjay”:66, “Sagar”:88}

# --------------------------
# list1 = ["red", "green", "blue"]
# list2 = ["#FF0000", "#008000", "#0000FF"]

# dict1 = {list1[i]: list2[i] for i in range(len(list1))}
# print(dict1)

# a = ["Anirudh", "Sanjay", "Sagar"]
# b = [33, 66, 88]

# dict2 = {a[i]: b[i] for i in range(len(a))}
# print(dict2)


# # --------------------------------------------------
# # Q4. Write a Python program to convert string values of a given dictionary into integer/float data types.
# #
# # Example 1:
# # Original list:
# # [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# #
# # Output:
# # [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
# #
# # Example 2:
# # Original list:
# # [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
# #
# # Output:
# # [{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]

# ---------------------------
my_list = [
    {"x": "10.12", "y": "20.23", "z": "30"},
    {"p": "40.00", "q": "50.19", "r": "60.99"},
]
result = []
for d in my_list:
    r = {}
    for k, v in d.items():
        if "." in v:
            r[k] = float(v)
        else:
            r[k] = int(v)
    result.append(r)
print(result)
# ---------------------------
# original_list = [{"x": "10", "y": "20", "z": "30"}, {"p": "40", "q": "50", "r": "60"}]

# for dictionary in original_list:
#     for key in dictionary:
#         if "." in dictionary[key]:
#             dictionary[key] = float(dictionary[key])
#         else:
#             dictionary[key] = int(dictionary[key])

# print(original_list)
##################?????????????????????????????????????

# # --------------------------------------------------
# # Q5. Write a Python program to convert a dictionary into a list of lists.
# #
# # Example 1
# # Original Dictionary:
# # {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# #
# # Result:
# # [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
# #
# # Example 2
# # Original Dictionary:
# # {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# #
# # Result:
# # [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]

# --------------------------

# original_dict = {1: "red", 2: "green", 3: "black", 4: "white", 5: "black"}

# list_of_lists = [[key, value] for key, value in original_dict.items()]

# print(list_of_lists)

# #---------------
# original_dict = {
#     "1": "Austin Little",
#     "2": "Natasha Howard",
#     "3": "Alfred Mullins",
#     "4": "Jamie Rowe",
# }

# list_of_lists = [[key, value] for key, value in original_dict.items()]

# print(list_of_lists)


# # --------------------------------------------------
