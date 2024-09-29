# Three cyclists are riding at the speed of 10,20,30 km/h. find the average and compare which cyclist is riding slower than the average speed?
first = 10
second = 20
third = 30

sums = first+second+third
average = sums//3
if average > first and average > second and average > third:
    print("average is greater then all")
elif average > first and average > second:
    print("average is greater than first and second")
elif average > second and average > third:
    print("average is greater than second and third")
elif average > first:
    print("average is greater tgan first")
elif average > second:
    print("average is greater than second")
elif average > third:
    print("average is greater than third")
input("press enter to leave")


