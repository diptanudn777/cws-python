a = [-54, -65, -34, -43, -32, -56, -43]
smallest = a[0]
for i in range(0, len(a)):
    if a[i] < smallest:
        smallest = a[i]
print(smallest)
