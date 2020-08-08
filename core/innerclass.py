class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print('\n##########################')
        print(self.name, self.rollno)
        print(self.lap.show())
        return ""

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)
            return ""


s1 = Student('Python1', 1)
s2 = Student('Python2', 2)

lap1 = s1.lap
lap2 = s2.lap

print(s1.name, s2.name)
print(s1.show(), s2.show())
print(lap1.show())
print(lap1.brand, lap1.cpu, lap1.ram)
print(s1.lap.brand, s1.lap.cpu, s1.lap.ram)
print(s1.lap.show())
# print(s1.lap1.brand, s1.lap1.cpu, s1.lap1.ram)
print(lap2.show())
print(lap2.brand, lap2.cpu, lap2.ram)
print(s2.lap.brand, s2.lap.cpu, s2.lap.ram)
print(s2.lap.show())