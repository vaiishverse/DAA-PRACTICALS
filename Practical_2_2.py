# Practical 2 - Access Matrix Recursively

def show(a, i, j):
    if i == len(a):
        return

    print(a[i][j], end=" ")

    if j == len(a[0]) - 1:
        print()
        show(a, i + 1, 0)
    else:
        show(a, i, j + 1)


r, c = map(int, input("Enter rows and columns: ").split())

a = [list(map(int, input("Enter row: ").split())) for _ in range(r)]

print("Matrix:")
show(a, 0, 0)