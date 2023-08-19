a = {
    "Anirudh": [34, 15, 74, 88, 11],
    "Sanjay": [75, 12, 11, 89, 77],
    "Akul": [73, 99, 90, 91, 11],
    "Nihar": [55, 43, 19, 83, 67],
    "Karan": [77, 84, 21, 22, 20],
}

"""
Anirudh has highest marks = 88

With MAX()
Without MAX()
"""
# for k, v in a.items():
#     print(f"{k} has highest marks {max(v)}")

for k, v in a.items():
    max_num = a[k][0]
    for num in a[k]:
        if num > max_num:
            max_num = num
    print(f"{k} has highest marks {max_num}")
