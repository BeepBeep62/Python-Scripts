ch=input("Enter a character:  ")
if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    print("This is an alphabet.")
elif(ch>='0' and ch<='9'):
    print("This is a number.")
else:
    print("This is a special character.")
input("press enter to leave")