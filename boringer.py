# Create a python program to create a flashcard using object-oriented programming. A flashcard is a two-sided card with information on both sides that can assist memory. A question and an answer are usually printed on one side of a flashcard. Follow these steps to complete the activity - 1. From the user, take the input for a word and its definition. 2. To assign values for Word and Meaning, create a class called flashcard and use the __init__() function. 3. We'll use the __str__() function to get a string with the term and its definition. 4. Save the strings that have been returned in a list. 5. To print all of the stored flashcards, use a while loop.
flash = []
print("welcome to fth flash card game")
class flashcard:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition
    def __str__(self):
        return self.word + self.definition
while True:
    word = input("enter ur word u want to add in ur flashcard: ")
    definition = input("enter the definition of your word that u want to add in ur flash card: ")
    flash.append(flashcard(word, definition))
    option = int(input("enter 0 if you want to add another flashcard, otherwise, enter 1. "))
    if option == 1:
        break
for i in flash:
    print("your flashcard has recieved", i)