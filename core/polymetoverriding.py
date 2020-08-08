#  3. Method Overriding


class A:

    def show(self):
        print('\n Class A show')

class B(A):
    pass

    def show(self):
        super().show()
        print('\n Class B show')

class C(B):

    def show(self):
        print('\n Class C show')

a1 = A()
a1.show()

b1 = B()
b1.show()

c1 = C()
c1.show()