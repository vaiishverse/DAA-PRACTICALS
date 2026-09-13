# Practical 2 - Insert Element in Array

arr = list(map(int, input("Enter elements: ").split()))

pos = int(input("Position: "))
val = int(input("Value: "))

arr.insert(pos - 1, val)

print("Array after insertion:", arr)