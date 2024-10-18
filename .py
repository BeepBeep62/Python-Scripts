# Write a program using nested while loop. If the value is divided by two, then it will run an infinite loop of the bye.
num = int(input("enter numbscull: "))
valid = False
while valid==False:
    try:
        num = int(input("enter numbscull: "))
        while num%2==0:
            print("bye bye") or print("bye") or print(1,100000)
        valid = True
    except ValueError:
        print("invalid value")