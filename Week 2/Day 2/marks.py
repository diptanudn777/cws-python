"""
Ask 3 marks from user. out of 100

If pass in all subjects
Then only print total percentage

FAIL

pass marks 33
"""

m1 = int(input("Enter the sub1 marks: "))
m2 = int(input("Enter the sub2 marks: "))
m3 = int(input("Enter the sub3 marks: "))

if m1 >= 33 and m2 >= 33 and m3 >= 33:
    total = m1 + m2 + m3
    percentage = (total / 300) * 100
    print(f"Total = {total} and percentage = {percentage:.2f}%")
else:
    print("Fail")
