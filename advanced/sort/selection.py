
def selectionsort(nums):

    for i in range(len(nums)):
        minpos = i
        for j in range(i ,len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j

        nums[i], nums[minpos] = nums[minpos], nums[i]

        print(nums)

    return nums


arr = [5, 8, 4, 6, 9, 1, 10, 11, 7, 6, 1, -1, -5]
print('################')
print(arr)
print('################')
selectionsort(arr)
print('################')
print(arr)
