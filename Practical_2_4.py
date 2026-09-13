# Practical 2 - Transpose Matrix

r, c = map(int, input("Enter rows and columns: ").split())

a = [list(map(int, input("Enter row: ").split())) for _ in range(r)]

print("Transpose Matrix:")

for j in range(c):
    for i in range(r):
        print(a[i][j], end=" ")
    print()