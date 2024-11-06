# Write a program to return - 1. zipped list from two lists 2. elements of two lists zipped together, but 2nd list in reverse order 3. elements of two lists zipped into a dictionary
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l3 = zip(l1,l2[::-1])
print(list(l3))
print(l2[::-1]) 