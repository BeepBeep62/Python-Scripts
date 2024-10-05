num = int(input("ENTER A NUMBER NOWWWWWWWWWWWWWWWWWWWWWWWW: "))
digits = 0
imstrong = 0
temp = num
while(num!=0):
    num = num//10
    digits = digits+1
print(digits)
num=temp
while(num!=0):
    last = num%10
    mul = last**digits
    num=num//10
    imstrong+=mul
if temp==imstrong:
    print("this is amstrong number")
else:
    print("this is not")
input("")
