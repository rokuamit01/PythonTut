class Student:

    schoolname = "Python Academy"
    studentcount = 0

    def __init__(self, name, subject, rollno):
        self.name = name
        self.subject = subject
        self.rollno = rollno
        m1 =0
        m2 =0
        m3 =0
        Student.studentcount = Student.studentcount + 1

    def setmarks(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def getaverage(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def getstudentinfo(self):
        print('This student info is: School Name# {}, Name# {}, Subject# {}, Roll# {}'.format(Student.schoolname, self.name, self.subject, self.rollno), end="")
        return ""

    @classmethod
    def getSchoolName(cls):
        return cls.schoolname

    @staticmethod
    def info():
        print('This is Student class. No of students enrolled is {}'.format(Student.studentcount))
        return ""


s1 = Student("Raj", "Science", 100)
s1.setmarks(100, 200, 300)
s2 = Student("Raju", "Bio", 101)
s2.setmarks(200, 300, 400)
s3 = Student("Rajesh", "Commerce", 102)
s3.setmarks(75, 200, 25)
print(s1.getstudentinfo())
print(s1.getaverage())
print(s2.getstudentinfo())
print(s2.getaverage())
print(s3.getstudentinfo())
print(s3.getaverage())
print(Student.getSchoolName())
print(Student.info())

