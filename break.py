""" Break
Outline:
Write a program to check alphabet “A” is present in the given string or not. And terminate the loop after finding the alphabet “A.” """
word = input("DO SOMETHUBGNG: ")
i = (len(word))
for letter in word:
    print(letter)
    if letter == "A" or letter == "a":
        print("A is present")
        break