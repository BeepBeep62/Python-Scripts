# Write a program to calculate the number of notes in the given amount?
amount = int(input("enter number to calculate number of notes: ")) # 
notesofhundred = amount//100
print("notes of hundred:",notesofhundred)
notesofifty = (amount%100)//50
print("notes of fifty:",notesofifty)
notesoften = ((amount%100)%50)//10
print("notes of ten:",notesoften)
notesofive = (((amount%100)%50)%10)//5
print("notes of five:",notesofive)
notesoftwo = ((((amount%100)%50)%10)%5)//2
print("notes of two:",notesoftwo)