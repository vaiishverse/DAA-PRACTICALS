# Practical 3 - Question 1
# Linear Search

a = list(map(int, input("Enter elements: ").split()))

key = int(input("Enter element to search: "))

found = False

for i in range(len(a)):
    if a[i] == key:
        print("Found at position", i)
        found = True
        break

if not found:
    print("Not Found")