# Write a program to check the frequency of a value in a dictionary - {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}.
codingal = {
    'Codingal' : 2, 
    'is' : 2, 
    'best' : 2, 
    'for' : 2, 
    'Coding' : 1
    }
howmanyapples = 100
count = 0
for u in codingal:
    if codingal[u]==howmanyapples:
        count = count+1
print(count)