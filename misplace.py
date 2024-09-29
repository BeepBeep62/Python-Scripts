# The mean of 40 numbers is 38. Later on, I detected that I misread the number 56 as 36. Find the correct mean of given numbers.
mean = 38
total = 40
incorrectsum = mean*total
correctsum = incorrectsum-36+56
newmean = correctsum/total
print(newmean)