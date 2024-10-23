# Write a Python program to count the number of strings where the string length is two or more, and the first and last characters are the same from a given list of strings.
ratings = ["A", "AZ", "AAZ", "AAZZ", "ZZ", "ZZZ", "Z"]
lvl2 = []
for r in ratings:
    if len(r) >= 2:
        lvl2.append(r)
print(lvl2)
for l in lvl2:
    if l[0]==l[-1]:
        print("you win :",l)