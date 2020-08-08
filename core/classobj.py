# Classes and Objects in Python - instance variables, static/class variables


class Computer:

    salescount = 0

    def __init__(self, cpu, ram, memory):
        print('Inside __init__')
        self.cpu = cpu
        self.ram = ram
        self.memory = memory
        self.brand = 'HP'
        Computer.salescount += 1


    def updatebrand(self, brand):
        self.brand = brand
        return ""

    def config(self):
        print('This machine configured with {}, {}, {} and {}'.format(self.cpu, self.ram, self.memory, self.brand), end="")
        return ""

    def getsalescount(self):
        print("No of machines sold is: ", Computer.salescount, end="")
        return ""

print("\n######################################")
c1 = Computer('i5', '16GB', '1TB')
print(c1.config())
# print(type(c1))
print(id(c1))
print(c1.cpu)
print(c1.brand)
print(c1.getsalescount())

print("\n######################################")
c2 = Computer('i3', '8GB', '1TB')
print(c2.config())
# print(type(c2))
print(id(c2))
print(c2.cpu)
print(c2.brand)
c2.updatebrand("Dell")
print(c2.config())
c2.updatebrand("Lenova")
print(c2.config())
print(c2.getsalescount())

print("\n######################################")
c2 = Computer('i7', '16GB', '2TB')
print(c2.getsalescount())