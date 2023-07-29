# x = int(input("Enter the 1st number: "))
# y = int(input("Enter the 2nd number: "))
# print(f"The sum of {x},{y} is: {x+y}")

# x = float(input("Please enter the speed of car in Kilometer as a unit: "))
# rounded_miles = round(x * 0.621371, 2)
# print(f"The speed value of car in Miles= {rounded_miles} miles")

# x = float(input("Enter the 1st number: "))
# y = float(input("Enter the 2nd number: "))
# z = float(input("Enter the 3rd number: "))
# print(f"The average of {x},{y},{z} is: {(x+y+z)/3}")

# x = float(input("Please enter the value in Rupees as a unit: "))
# rounded_paise = round(x * 100, 2)
# print(f"The amount entered in Paise= {rounded_paise} paise")

# x = float(input("Enter the length of 1 side of the square: "))
# print(f"The Area of the square is: {x**2}")

# Calculate number of tie and total Points. (1 win= 4 points, 1 tie =2 points)

x = int(input("Enter the number of games played: "))
y = int(input("Enter the number of games won: "))
z = int(input("Enter the number of games loss: "))
tie = int(x - (y + z))
print(f"Number of tie = {tie}")
print(f"Total points = {(x*4)+(tie*2)}")
