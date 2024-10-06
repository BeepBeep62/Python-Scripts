lower = int(input("enter lower number: "))
upper = int(input("enter upper number: "))
prime = 1
for num in range(lower,upper):
    if num >1:
        for i in range (2,num):
            if num%i==0:
            
                prime = 0
                break
        if prime==1:
            print(num,"is a PRIME NUMBER!")
input("")