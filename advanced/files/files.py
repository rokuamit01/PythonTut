f1 = open("TestData", 'r')
print(f1)

print("\n###################")
print(f1.readline(), end="")
print(f1.readline(), end="")
print("\n###################")
print(f1.read())

print("\n###################")

f2 = open("TestData", 'r')
print(f2.read())
print("\n###################")
print(f2.readline())

f3 = open("TestData1", 'w')
f3.write("Something")
f3.write(" Writing")
print("\n###################")

f4 = open("TestData2", 'a')
f4.write("\n")
f4.write("Something")
f4.write(" Writing")
print("\n###################")

f5 = open("TestData", 'r')
f6 = open("TestData3", 'w')
for data in f5:
    f6.write(data)

f7 = open("Python.jpg", 'rb')
f8 = open("PythonCopy1", 'wb')
for data in f7:
    print(data)
    f8.write(data)
