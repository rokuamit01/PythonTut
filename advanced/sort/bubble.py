

def bubblesort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


arr = [5, 8, 4, 6, 9, 1, 10, 11, 7, 6, 1]
print(arr)
print(bubblesort(arr))
