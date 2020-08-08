#  2. Operator Overloading


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        obj = Student(m1, m2)
        return obj

    def __gt__(self, other):
        val1 = self.m1 + self.m2
        val2 = other.m1 + other.m2
        if val1 > val2:
            return True
        else:
            return False

    def __str__(self):
        return '{}, {}'.format(self.m1, self.m2)


s1 = Student(70, 31)
s2 = Student(60, 40)

s3 = s1 + s2

print(s3.m1, s3.m2)

if s1 > s2:
    print('S1 wins')
else:
    print('S2 wins')

print(s3)
