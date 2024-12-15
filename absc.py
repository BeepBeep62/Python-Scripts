# Write a program to create a base class that consists of two functions - one to display a value, and another function is an abstract method. Next, create a subclass that consists of a method similar to the abstract method. Finally, showcase how Abstraction is being implemented in this example.
from abc import ABC, abstractmethod
import random
# I create basw class kok
class lol(ABC):
    def printvalue(self, val):
        print("yeah im printing the value", val)
    # creating absracyt mertyhjodf
    @abstractmethod 

    def jk(self):
        print("i am abstract method and i am wicked and broke as i dwell into the wretched aethos")
class lolol(lol):
    def jk(self):
        print("i am inside a base class and i am wicked and broke as i dwell into the wretched aethos")
objectovallicoracorocanisis = lolol()
objectovallicoracorocanisis.jk()
objectovallicoracorocanisis.printvalue(random.randint(2001,2019))