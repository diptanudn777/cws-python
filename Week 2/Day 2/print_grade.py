"""
Ask 1 mark

91-100 -> A
81-90 -> B
71-80 -> C
61-70 -> D
0-60 -> E

Invalid
"""

m = float(input("Enter marks = "))
# if m >= 91 and m <= 100:
if 91 <= m <= 100:
    print("A")
elif m >= 81 and m <= 90:
    print("B")
elif m >= 71 and m <= 80:
    print("C")
elif m >= 61 and m <= 70:
    print("D")
elif m >= 0 and m <= 60:
    print("E")
else:
    print("Invalid")
