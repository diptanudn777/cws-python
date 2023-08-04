a = [22, 54, 65, 76, 564, 43, 11]

print(a)

# del a[2]
del a[-1]
print(a)

a.pop(
    0
)  # if not mentioned position it'll delete last one by default #you need to pass pos
print(a)

a.remove(57)  # you need to pass values
print(a)
