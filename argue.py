# Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total amount you should pay.
pay1 = int(input("amount: "))
tip = int(input("percentage: "))
def totalcalc(amount, tiperc):
    temp = ((amount*tiperc)//100) 
    return temp + amount
print(totalcalc(pay1, tip))