arr = list(map(int, input("Enter elements: ").split()))
x = int(input("Enter element to search: "))

found = False
for i in range(len(arr)):
    if arr[i] == x:
        print("Element found at index", i)
        found = True
        break
if not found:
    print("Element not found")