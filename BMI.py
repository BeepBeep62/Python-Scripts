""" A body mass index (BMI) chart categorizes weight based on BMI ranges:
Underweight: Less than 18.5

Healthy weight: 18.5–24.9

Overweight: 25–29.9

Obesity: 30 and above"""
WEIGHT = int(input("enter your weight in kilograms: "))
HEIGHT = int(input("enter your height in centimeters: "))
BMI = WEIGHT/(HEIGHT/100)**2
if BMI <= 18.5:
 print("underweight BMI")
elif BMI >= 18.5 and BMI <= 24.9:
 print("Healthy weight")
elif BMI >= 25 and BMI <= 29.9:
 print("overweight")
else:
 print("obese")
