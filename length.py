word = input("please enter a word: ")
# Write a program to check how many times a character is repeated in a word?
ch = input("what character do you want to check was repeated: ")
index = 0
count = 0
while(index<len(word)):
    if word[index]==ch:
        count=count+1
    index=index+1
print("character has repeated",count,"times")
input("press enter to leave")