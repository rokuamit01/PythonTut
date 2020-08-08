#  Abstract Base Class

from abc import ABC, abstractmethod


class Computer(ABC):

    @abstractmethod
    def process(self):
        pass

    def brand(self):
        print('Computer brand is always HP.')


class Laptop(Computer):

    def process(self):
        print('Computer Type - Laptop')


class Whiteboard(Computer):

    def write(self):
        print('Writing')

    def process(self):
        print('Whiteboard Type')


class Programmer(Computer):

    def work(self, obj):
        print('Solving bugs')
        obj.process()

    def process(self):
        print('Programmer Type')


print('\n###################')
l1 = Laptop()
l1.process()
l1.brand()

print('\n###################')
w1 = Whiteboard()
w1.process()
w1.write()
w1.brand()

print('\n###################')
p1 = Programmer()
p1.process()
p1.brand()
p1.work(l1)
p1.work(w1)


