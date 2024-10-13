n1 = int(input("enter number,: "))
n2 = int(input("enter number2: ,"))
def divcube(n1):
    return n1*n1*n1
def divcheck(n1, n2):
    if n1%n2==0:
        return True
    else:
        return False
if divcheck(n1, n2)==True:
    print(n1,"IS DIVIDBLE BY",n2) 
    print(divcube(n1))
else:
    print(n1,"NOT DIVSIBLE by",n2)
# define another function which let execute the cube function if the number is divisible by 3
# cube is when you multiply same number 3 times for 3 times in a 3 times, for example 2x2x2 and 4x4x4 and 9x9x9 and 100x100x100
