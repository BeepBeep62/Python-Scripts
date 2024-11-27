# Write a program to create a class IOString which consists of a constructor that gives a default value to variable str1. Next up create a method that gets a string as input from the user. Create another method that will print the string in the upper case. Next up create an object and call methods to get everything implemented.
class IOString:
    # vcreate constructer with default value
    def __init__(self):
        self.strre = ""
    def takinginput(self):
        # the input you aere taking shoulds be stored in tside the deufaulyt variavble
        self.strre = input("enter some something: ")    
    def uppercause(self):
        print(self.strre.upper())
facade = IOString()
facade.takinginput()
facade.uppercause()