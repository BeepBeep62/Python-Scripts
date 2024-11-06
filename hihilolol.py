# Write a program to return the addition of numbers of two different lists. Then, display a list that is square of numbers of another list. Use the map() function here to get the desired result.
l1 = [1, 4, 8, 9, 7, 6, 3, 2]
l2 = [7, 8, 5, 1, 3, 4, 0, 9]
def square(n):
    return n*n
# the output for theze R = [8, 12, 13, 10, 10, 10, 3, 11]
NEWLIST = map(lambda x, y: x+y, l1, l2)
print(list(NEWLIST))
n = [1, 2, 3]
squad = map(square,n)
print(list(squad))