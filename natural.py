# Write a program to find the sum of natural numbers.
# lets say if i add the 5 here what will be the answer  answer willl be 1+2+3+4+5=15 yes answer
i = int(input("what do you wnat number: "))
nanosum = 0
count = 1
while(count<=i):
    nanosum += count
    count = count+1
print(nanosum)
