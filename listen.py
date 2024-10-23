# Write a Python program to find the sum and average of the list. The average of the list is defined as the sum of the elements divided by the number of the elements. Also, find the largest and the smallest number in the list
erm = [1, 0.3, 2763, 2, 700, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 10, 2.5, 5, 6, 7, 8, 9, 2, 2, 2, 2, 200]
sumer = 0
count = 0
for num in erm:
    count = count+num
avg = count/len(erm)
print(avg)
print(max(erm))
print(min(erm))
print(erm.sort(reverse=True))
print(erm.count(2))
erm.append(900)
erm.insert(0, 90000)
print(erm)
erm.remove(900)
print(erm)
input("")