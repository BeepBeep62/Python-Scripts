# Write a program where the value of i begins from 1 and goes to 10. When the value of i becomes 5, force the interpreter to exit the program
for i in range(1, 10+1):
    if i == 5:
        print("exiting")
        exit()
    print(i)