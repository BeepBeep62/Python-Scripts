# Write a program to illustrate the use of 'is' identity operator
a = [1,2,3,4]
b = [1,2,3,4]
print(a is b)
c = a
print(c is a)
print(c is not a)