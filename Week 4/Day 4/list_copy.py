a = [100, 211, 113, 4, 76, 73, 13]
b = a
c = a.copy()

print(id(a))
print(id(b))
print(id(c))

print(a)
print(b)

a.append(100)

print(a)
print(b)
