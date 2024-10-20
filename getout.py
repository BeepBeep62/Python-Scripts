# Write a program to calculate the total trip expenditure: Calculate the hotel cost per day Calculate the plane cost Price of the vehicle rented during the trip
def hotelprice(nights):
    return 100*nights
def planeride():
    return 1000
def car(days):
    if days >= 7:
        return 100*days
    elif days >= 3:
        return 150*days
    else:
        return 200*days
nights = int(input("enter for how many nights you want the hotel it is  : ?:"))
planer = input("do you want plane ride yes or no: ")
days = int(input("how much days you wantt to rent car: "))
total = hotelprice(nights)+car(days)
if planer == "yes" or "Yes" or "y" or "Y":
    print(total+planer)
else:
    print(total)
