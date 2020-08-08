from numpy import *

print('\n##############################')
arr = array([1, 2, 3, 4, 5, 4.0])
print(arr)
print(arr.dtype)

arr = array([1, 2, 3, 4, 5, 4],int)
print(arr)
print(arr.dtype)

print('\n##############################')
arr = linspace(0,15,20)
print(arr)
print(arr.dtype)

arr = linspace(0,15)
print(arr)
print(arr.dtype)

print('\n##############################')
arr = arange(1,15,2)
print(arr)
print(arr.dtype)

print('\n##############################')
arr = logspace(1,40,5)
print(arr)
print(arr.dtype)
print('%.2f' %arr[0])
print('%.2f' %arr[4])

print('\n##############################')
arr = zeros(5)
print(arr)
print(arr.dtype)

arr = zeros(5,int)
print(arr)
print(arr.dtype)

print('\n##############################')
arr = ones(5)
print(arr)
print(arr.dtype)

print('\n##############################')
arr = array([1, 2, 3, 4, 5])
print(arr)
print(arr.dtype)
arr = arr + 5
print(arr)

print('\n#############VECTORIZED OPERATION#################')
arr1 = array([1, 2, 3, 4, 5])
arr2 = array([5, 4, 3, 2, 1])
arr3 = arr1 + arr2
print(arr3)
print(sum(arr3))
print(min(arr1))
print(max(arr1))
print(sqrt(arr1))
print(sin(arr1))
print(cos(arr1))
print(log(arr1))
print(concatenate([arr1,arr2]))

arr4 = arr1
print(arr4)
print(id(arr1))
print(id(arr4))

arr4 = arr4 + 1
print(arr4)
print(id(arr1))
print(id(arr4))

arr4 = arr1.view()
print(arr4)
print(id(arr1))
print(id(arr4))

print('\n#############SHALLOW COPY#################')
arr4 = arr1.view()
arr1[1] = 8
print(arr1)
print(arr4)
print(id(arr1))
print(id(arr4))

print('\n#############DEEP COPY#################')
arr4 = arr1.copy()
arr1[1] = 2
print(arr1)
print(arr4)
print(id(arr1))
print(id(arr4))
