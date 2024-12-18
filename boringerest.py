import random
# Write a program to create a quiz related to multiple fruits using object-oriented programming in Python. Create a class that consists of - 1. a constructor with a dictionary of fruits and respective colours 2. a function to execute the quiz. Here, the fruit will be chosen at random from the dictionary. Then ask the user to enter the colour of that fruit. Evaluate the answer and display the result accordingly.
class fruitquizgameio2012:
    def __init__(self):
        self.fruits = {
            "apple": "red",
            "banana": "yellow",
            "orange": "orange",
            "grapes": "green",
            "blueberry": "blue"
        }
    def gquiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            print("what is the color of {}".format(fruit))
            ans = input("")
            if ans.lower()==color:
                print("correct answer")
            else:
                print("WRONG! GET REEDUCATED")
            option = int(input("enter 0 if you want to continue game, otherwise, enter 1. "))
            if option == 1:
                break
fruit = fruitquizgameio2012()
fruit.gquiz()