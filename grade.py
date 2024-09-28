# Outline: Write a program to show students' grades by entering five subject marks and calculating average marks and grades. For example, if the average is between 91 to 100, A2 is between 81 to 90, and so on, do it till grade E2?
print("input in your 5 subject grades: ")
math = int(input("enter math: "))
science = int(input("enter science: "))
english = int(input("enter english: "))
urdu = int(input("enter urdu: "))
python = int(input("enter py: "))
sumed = math + urdu + english + science + python
avg = sumed/5
if avg >= 91 and avg <= 100:
 print("A+ grade")
elif avg >= 81 and avg <= 91:
 print("A grade")
elif avg >= 70 and avg <= 81:
 print("B+ grade")
elif avg >= 60  and avg <= 70:
 print("B grade")
elif avg >= 50  and avg <= 60:
 print("B- grade")
elif avg >= 40  and avg <= 50:
 print("C+ grade")
elif avg >= 30  and avg <= 40:
 print("C grade")
elif avg >= 20  and avg <= 30:
 print("C- grade")
else:
 print("F grade")
 input("press enter to leave")