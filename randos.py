# Write a program to generate a random integer and match it with the input given by the user?
import random
computernumber = random.randint(1,10)
while(True):
    usernumber = int(input("guess a number between 1 to 10: "))
    if usernumber == computernumber:
        print("you win ok nsksfjskodewl,a")
        break
    else:
        print("try again")