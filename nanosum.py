# Write a program to make a calculator : For making a calculator create four functions add, subtract, multiply, divide. Ask for a choice from users which operation they want to perform. Take user input whatever operation they want to perform And call that function accordingly
print("calculqtor")
n1 = int(input("what do you wanrt first numbah: "))
n2 = int(input("what do you wanrt second numbah: "))
ops = input("WHAT THE HECK YOU WANT TO PERFORM OPERSATION SYMBOL MATH: ")
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def divide(n1, n2):
    return n1 / n2
def multiply(n1, n2):
    return n1 * n2
def mod(n1, n2):
    return n1 % n2
if ops == "+":
    print("your sum is", add(n1, n2))
elif ops == "-":
    print("you r sum is ", subtract(n1, n2))
elif ops == "/":
    print("ur sum sis si", divide(n1, n2))
elif ops == "*" or ops == "x":
    print("yor anssdm izs e", multiply())
elif ops == "%" or ops == "mod":
    print("UR ANSWER IS ,", mod(n1, n2))
else:
    print("what did bro type")
input("")