# rit a program to create an array with the following elements - [1, 3, 5, 3, 7, 9, 3]. Then find the number of occurrences of number 3 in the array. Also, print the reversed array.
import array as arr
num = arr.array("i", [1, 3, 5, 3, 7, 9, 3])
print(num)
print(num.count(3))
num.reverse()
print(num,)