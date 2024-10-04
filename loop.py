# Write a program to calculate the sum of whole numbers.
nums = int(input("how many numbers you want to do sum of"))
sume = 0
for num in range(1, nums+1):
    sume=sume+num
print(sume)