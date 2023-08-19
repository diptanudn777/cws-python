# # case 1:
# num1, num2 = list(map(int, input("Enter numbers = ").split()))
# print(num1 + num2)

# Case 2:
t = int(
    input("Enter number of cases = ")
)  # don't mention: "Enter number of cases = ", then this will be in input in Codechef, and will through error

for i in range(0, t):
    num1, num2 = list(map(int, input("Enter numbers = ").split()))
    print(num1 + num2)
