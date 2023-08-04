a = [54, 2, 1, 43, 676, 45, 54, 21, 1787, 2, 45]
b = []
##to get the unique count of a's elements, but we'll iterate b

for i in a:
    if i not in b:
        b.append(i)

for i in b:
    print(f"{i} comes in list {a.count(i)} times")

# ---------------------------
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

# ---------------------------
# if 45 in a:
#     print("Yes")
# else:
#     print("No")
# ----------------------------
