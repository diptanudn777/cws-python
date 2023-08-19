a = {
    "Anirudh": [34, 15, 74, 88, 11],
    "Sanjay": [75, 12, 11, 89, 77],
    "Akul": [73, 99, 90, 91, 11],
    "Nihar": [55, 43, 19, 83, 67],
    "Karan": [77, 84, 21, 22, 20],
}

"""
Anirudh has scored 444 marks
Sanjay has scored 444 marks
Akul has scored 444 marks
Nihar has scored 444 marks

MEthod 1 - With using SUM()
MEthod 2 - Without using SUM()
"""
# for k, v in a.items():
#     print(f"{k} has scored {sum(v)}")

for k, v in a.items():
    total = 0
    for m in v:
        total += m  # to reset the total for everyone
    print(f"{k} has scored {total} marks")
