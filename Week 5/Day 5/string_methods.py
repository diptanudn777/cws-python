a = ".         hello        "

print(a)
print(len(a))

a = a.strip()
print(a)
print(len(a))

a = "pttttttttttttttthellotttttttttttttt"
a = a.strip("t")
print(a)
print(len(a))


a = "ttttttttttttttthellotttttttttttttt"
a = a.lstrip("t")
print(a)
print(len(a))

a = "ttttttttttttttthellotttttttttttttt"
a = a.rstrip("t")
print(a)
print(len(a))
