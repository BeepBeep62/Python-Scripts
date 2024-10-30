words = {
    'Codingal' : 4, 
    'is' : 2, 
    'best' : 8, 
    'for' : 2, 
    'Coding' : 4
    }
howmanyapples = int(input("which you wanna check numbers: "))
count = 0
for u in words:
    if words[u]==howmanyapples:
        count = count+1
print(count)