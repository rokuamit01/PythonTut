# 1. Duck Typing


print('\n###################')
x = 5
print(x)
print(type(x))
x = 'Python'
print(x)
print(type(x))


class PyCharm:

    def execute(self):
        print('\n###################')
        print('\nPyCharm IDE',end="")
        print('\nCompiling',end="")
        print('\nExecuting')

class MyEditor:

    def execute(self):
        print('\n###################')
        print('\nMyEditor IDE',end="")
        print('\nSpelling Check',end="")
        print('\nPlug-ins Check',end="")
        print('\nCompiling',end="")
        print('\nExecuting')


class Laptop:

    def code(self, ide):
        ide.execute()


lap1 = Laptop()

pc1 = PyCharm()
lap1.code(pc1)

med1 = MyEditor()
lap1.code(med1)