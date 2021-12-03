# n = int(input("Enter the number of rows for Rhombus:"))
# for i in range(0, n):
#     for j in range(1, n - i):
#         print(" ", end='')
#     for k in range(0, n):
#         print("*", end='')
#     print()

n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * n)
