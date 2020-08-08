from numpy import *

print('\n##############################')
arr = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr1 = array([1, 2, 3, 4, 5])
arr2 = array([5, 4, 3, 2, 1])

arr3 = array([
                [1,2,3],
                [4,5,6]
            ])

arr4 = array([
                arr1,
                arr2
            ])

print(arr1)
print(id(arr1))

print(arr2)
print(id(arr2))

print('\n##############################')
print(arr3)
print(id(arr3))
print(arr3.ndim)
print(arr3.dtype)
print(arr3.size)
print(arr3.flatten())

print('\n##############################')
print(arr4)
print(id(arr4))
print(arr4.flatten())

print('\n##############################')
print(arr)
arr5 = arr.reshape(3,4)
print(arr5)

print('\n##############################')
arr5 = arr.reshape(2,2,3)
print(arr5)

print('\n##############MATRIX################')
arr6 = matrix(arr.reshape(3,4))
print(arr6)

arr6 = matrix('1 2; 3 4')
print(arr6)

arr6 = matrix('1 2 3 4; 4 5 6 7')
print(arr6)

arr6 = matrix('1 2; 3 4; 4 5; 6 7')
print(arr6)

print('\n##############MATRIX################')
arr6 = matrix('1 2 3; 4 5 6; 7 8 9')
arr7 = matrix('1 2 1; 1 3 1; 1 4 1')
print(arr6)
print(arr7)
print(arr6.diagonal())
print(arr6.min())
print(arr6.max())
print(arr6 * 2)
print(arr6 * arr7)



