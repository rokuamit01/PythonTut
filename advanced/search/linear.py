arr = [5, 8, 4, 6, 9, 1, 10, 11]
searchVal = 10
found = False
pos = -1

print(arr)


def search(list, n):
    i = 0

    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i += 1
    return False


if search(arr, searchVal):
    print("Element found at ", pos + 1)
else:
    print("Element not found")

pos = -1
for i in arr:
    pos = pos + 1
    if i == searchVal:
        print("Element found at ", pos + 1)
        found = True
        break

if not found:
    print("Element is not found")
