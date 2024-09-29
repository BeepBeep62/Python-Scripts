# Write to check a number is divisible by another number.
numerator = int(input("enter numerator: "))
denomenator = int(input("enter denomenator: "))
if numerator%denomenator==0:
    print(str(numerator)+" is divisible by "+str(denomenator))
else:
    print(str(numerator)+" is not divisible by "+str(denomenator))
# divisible meaning if one is able to divide the second number and remainder is equal to 0