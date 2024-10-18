# Write a program to understand how the value error exception works?
try:
    num = int(input("ENTER A NUMBER"))
    print(num)
except ValueError as exception:
    print("invalid character")