# 1...
#  units = float(input("Enter units = "))
# rate = float(input("Enter rate = "))
# total_cost = units * rate
# total_cost += total_cost * 0.12
# if total_cost > 100 and total_cost % 5 == 0:
#     print(
#         f"The cost of your light bill is ${total_cost}. There is a free gift card to your favorite store."
#     )
# else:
#     print(f"The cost of your light bill is ${total_cost}.")

# 2...
# units = float(input("Enter units = "))

# if 0 < units <= 50:
#     total = units * 0.5
# elif 50 < units <= 150:
#     total = (50 * 0.5) + ((units - 50) * 0.75)
# elif 150 < units <= 250:
#     total = (50 * 0.5) + (100 * 0.75) + ((units - 150) * 1.2)

# else:
#     total = (50 * 0.5) + (100 * 0.75) + (100 * 1.2) + ((units - 250) * 1.5)

# print(f"Total = {total * (1+0.2)}")

# 3...
# print("Input lengths of triangle sides: ")
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))

# if a == b == c:
#     print("Equilateral triangle")
# elif a == b or b == c or a == c:
#     print("Isosceles triangle")
# else:
#     print("Scalene triangle")

# 4...
# num = int(input("Enter number to get the absolute value = "))
# print(f"The absolute value is = {abs(num)}")

# 5...
# char = str(input("Enter a character = ")).lower()
# if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
#     print("Vowel")
# else:
#     print("Consonant")

# 6...
print("Enter 3 numbers to get the largest one : ")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print(f"The largest number is = {max(a,b,c)}")
