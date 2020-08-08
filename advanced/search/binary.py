arr = [5, 8, 4, 6, 9, 1, 10, 11]
searchValue = 50
pos = -1

arr.sort()
print(arr)


def search(list, searchVal):
    lower = 0
    upper = len(list) - 1

    while lower <= upper:
        mid = (lower + upper) // 2

        if list[mid] == searchVal:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < searchVal:
                lower = mid + 1
            else:
                upper = mid - 1

#        return False


if search(arr, searchValue):
    print("Element found at ", pos + 1)
else:
    print("Element not found")
