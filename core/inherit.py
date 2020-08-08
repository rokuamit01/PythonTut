class A:

    def __init__(self):
        print('\n __init__ of Class A')

    def feature1(self):
        print("Class A - Feature 1 working")
        return ""

    def feature2(self):
        print("Class A - Feature 2 working")

    def feature(self):
        print("Class A - Feature working")
        return ""


class B:

    def __init__(self):
        print('\n __init__ of Class B')

    def feature3(self):
        print("Class B - Feature 3 working")
        return ""

    def feature4(self):
        print("Class B - Feature 4 working")
        return ""

    def feature(self):
        print("Class B - Feature working")
        return ""


class C(A, B):

    def __init__(self):
        super().__init__()
        print('\n __init__ of Class C')

    def feature5(self):
        print("Class C - Feature 5 working")
        return ""

    def feature6(self):
        print("Class C - Feature 6 working")
        return ""

class D(C):

    def __init__(self):
        print('\n __init__ of Class D')

    def feature7(self):
        print("Class D - Feature 7 working")
        return ""

    def feature8(self):
        print("Class D - Feature 8 working")
        return ""

class E(D):

    def feature9(self):
        print("Class D - Feature 9 working")
        return ""

    def feature10(self):
        print("Class D - Feature 10 working")
        return ""


print('\n##################')
a1 = A()
a1.feature1()
a1.feature2()

print('\n##################')
b1 = B()
b1.feature3()
b1.feature4()

print('\n##################')
c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
c1.feature6()
c1.feature()

print('\n##################')
d1 = D()
d1.feature1()
d1.feature2()
d1.feature3()
d1.feature4()
d1.feature5()
d1.feature6()
d1.feature7()
d1.feature8()

print('\n##################')
e1 = E()
e1.feature9()
e1.feature10()
