a = (1, 2, 3, 4, 5)

a = list(a)  # Overwrite
a.append(100)

print(a)

a = tuple(a)
print(a)
