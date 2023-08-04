a = [54, 2, 1, 43, 676, 45, 21, 45, 787, 4, 45]
num = 45

while True:
    c = a.count(num)  # 3
    if c == 0:
        break
    a.remove(num)

print(a)
