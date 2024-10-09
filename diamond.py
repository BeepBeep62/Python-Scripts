rows = int(input("how many rows: "))
midpoint = 0
if rows%2==0:
    midpoint=(rows//2)
else:
    midpoint=(rows//2)+1
spaces = midpoint-1
for r in range(1,midpoint+1):
    for s in range(1,spaces+1):
        print(" ",end="")
    num = 1
    for n in range(2*r-1):
        print(num,end="")
        num=num+1
    spaces=spaces-1
    print("")
spaces=1
for rick in range(1,midpoint):
    for sam in range(1,spaces+1):
        print(" ",end="")
    nums = 1
    for nym in range(1,2*(midpoint-rick)):
       print(nums,end="")
       nums=nums+1
    spaces=spaces+1
    print("")
input("")
    