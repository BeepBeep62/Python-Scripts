# Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not. If it's a palindrome, then it is the same after being reversed.
preep = 0
what = ("what the heck is a "+"palindrome")
coder = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9 , 8, 7, 6, 5, 4, 3, 2, 1)
print(what)
start = 0
end = len(coder)-1
while (start < end):
    if (coder[start]!= coder[end]):
        print("ITS NOT PALINDROME GRGRGRGRGR THAAATS ITTTT")
        preep = 1
        break
    start = start + 1
    end = end - 1
if preep == 0:
    print("palindrome.........................................................................................")