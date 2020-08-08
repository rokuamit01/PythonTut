#  Multi-tasking | Parallel Processing
from threading import *
from time import sleep


class Hello(Thread):

    def run(self):
        for i in range(5):
            print("\nHello",end="")
            sleep(1)

    def run2(self):
        for i in range(5):
            print("\nHello2",end="")
            sleep(1)


class Hi(Thread):

    def run(self):
        for i in range(5):
            print("\nHi",end="")
            sleep(1)


h1 = Hello()
h2 = Hi()
h1.start()
sleep(0.2)
h2.start()

h1.join()
h2.join()

print('\n#######BYE#########')