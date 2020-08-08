a = 5 # 101
b = 6 # 110

temp = a
a = b
b = temp

print('Value for a:', a)
print('Value for b:', b)
print('Value for temp:', temp)

a = a + b # 11 or 0b1010
b = a - b # 5
a = a - b # 6
print('Value for a:', a)
print('Value for b:', b)

a = a ^ b # 11
b = a ^ b # 5
a = a ^ b # 6
print('Value for a:', a)
print('Value for b:', b)

a,b = b,a
print('Value for a:', a)
print('Value for b:', b)

x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = x + y
print('Value for z:', z)

x = int(input("Enter 1st number: "))
y = float(input("Enter 2nd number: "))
z = x + y
print('Value for z:', z)

ch1 = input("Enter 1st character: ")
ch2 = input("Enter 2nd character: ")
z = ch1 + ch2
print('Value for z:', z)

ch1 = input("Enter 1st character: ")[0]
ch2 = input("Enter 2nd character: ")[0]
z = ch1 + ch2
print('Value for z:', z)

result = eval(input("Enter the expression: "))
print('Result is:', result)

