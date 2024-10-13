num = int(input("enter a number: "))
def factor(num):
    if num==1:
        return 1
    else:
        return num*factor(num-1)
print(factor(num))