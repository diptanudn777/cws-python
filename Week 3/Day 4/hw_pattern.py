"""
1st
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

try this like:
        *
      * *       *
    * * *       * *
  * * * *       * * *
* * * * *       * * * *
for
    for
    for
    for
"""
# for i in range(1, 6):
#     for j in range(5, i, -1):
#         print(" ", end=" ")

#     for k in range(1, i + 1):
#         print("*", end=" ")

#     for l in range(1, i):
#         print("*", end=" ")

#     print()

"""
2nd

        *
      * * *
    * * * * *
  * * * * * * * 
* * * * * * * * *
  * * * * * * * 
    * * * * *
      * * *
        *
for
    for
    for
    for

for
    for
    for
    for
"""
# for i in range(1, 6):
#     for j in range(5, i, -1):
#         print(" ", end=" ")

#     for k in range(1, i + 1):
#         print("*", end=" ")

#     for l in range(1, i):
#         print("*", end=" ")
#     print()

# for i in range(4, 0, -1):
#     for j in range(5, i, -1):
#         print(" ", end=" ")

#     for k in range(1, i + 1):
#         print("*", end=" ")

#     for l in range(1, i):
#         print("*", end=" ")

#     print()
"""
         
3rd

* * * * *
*       * 
*       * 
*       * 
* * * * *
"""
for i in range(1, 6):
    for j in range(1, 6):
        if i == 1 or i == 5 or j == 1 or j == 5:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
"""

4th

Ask a start number =
Ask a end number = 

Print all prime numbers between them.
"""
# start = int(input("Enter start number ="))
# end = int(input("Enter end number = "))
# for i in range(start, end + 1):
#     if i > 1:
#         for j in range(2, i):
#             if (i % j) == 0:
#                 break
#         else:
#             print(i, end=" ")
