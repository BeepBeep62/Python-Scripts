# check MEDICAL CONDITIONRF
medicalcon = input("do you have a diddly darn medical condition?? answer with Y or N: ")
if medicalcon =="N" or medicalcon =="n":
    attend = int(input("enter attendace:"))
    if attend >= 75:
        print("you aere allowed")
    else:
         print("u are not alowwed")
else:
    print("ur allowed")

