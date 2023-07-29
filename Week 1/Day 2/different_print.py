"""
different ways of print a variable
int(%d), float(%f), str(%s), bool
"""

# Myn name is ABC
# My age is 92
name = "ABC"
age = 92
gender = "Male"

# Method 1
print("My name is", name)
print("My age is", age)

# Method 2 (F-strings)
print(f"My name is {name} and my age is {age}")

# Method 3
print("My name is %s" % (name))
print("My name is %s and my age is %d" % (name, age))
# print("My name is %d and my age is %s" % (name, age))  # error, use the sequence

print("Hello World", name)
