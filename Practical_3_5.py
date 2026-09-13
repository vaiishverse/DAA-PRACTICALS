# Practical 3 - Question 5
# Insertion Sort

a = list(map(int, input("Enter elements: ").split()))

for i in range(1, len(a)):
    key = a[i]
    j = i - 1

    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1

    a[j + 1] = key

print(a)