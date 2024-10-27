# Write a program to perform the following operations: 1. Create a tuple with different datatypes 2. Create another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple 5. Perform slicing on the tuple
tup = (1, "lol", "yip", True, 1.80, 10, "ten")
inup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0,)
newt = inup + (9,)
print(newt.count(9))
print(newt[8:11])
print(newt[2:5])
print(newt[4:6])