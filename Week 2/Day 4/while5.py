"""
Ask start number from user (start) #5
Ask end number from user (end) #23

end to start
"""

s = int(input("Enter start number = "))
e = int(input("Enter end number = "))

while e >= s:
    print(e, end=" ")
    e = e - 1
