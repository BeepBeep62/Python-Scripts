# Write a program to implement abstraction on animal class (base class). The abstract method will be move will display what subclasses can do. Subclasses can be something like - Human, Dog.
from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("human walk, run, and get burned alive by a radioactive laptop")
class dawg(animal):
    def move(self):
        print("crawl")
objecrtoriebntwedprtuiogammkijnbg = human()
objecrtoriebntwedprtuiogammkijnbg.move()
lobejactoratiorgammingapramogosgb = dawg()
lobejactoratiorgammingapramogosgb.move()