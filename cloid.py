row = int(input("what how many letters u do what how many want bro: "))
num = 1
for rownum in range(1,row+1):
    for i in range(1,rownum+1):
        print(num,end="")
        num = num+1
    print("")