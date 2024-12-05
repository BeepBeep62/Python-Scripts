# Write a program to create a parent class Person (attributes - name, id number) with a method display to display the attributes. Next, create a child class Employee (attributes - name, id number, salary, post). Access the attributes of parent class in child class. Then, create an object for child class and call the display method to display the name and id number.
class person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        print(self.name, self.id)
class employee(person):
    def __init__(self, name, id, salary, post):
        self.salary = salary
        self.post = post
        #wanttotakeconstructor of persons class syehhhhh
        person.__init__(self, name, id)
e120 = employee('robert', 996127877, 19100, 'student')
e120.display()