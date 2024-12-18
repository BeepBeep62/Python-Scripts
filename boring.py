# Write a program to overload the less than (<) and equal to (==) operators. For example, create objects - ob1 and ob2 with values 3 and 4 to compare values, respectively. You can additionally create more objects to try different values.
class a:
    def __init__(self, n):
        self.n = n
    def __lt__(self, other):
        if self.n<other.n:
            return "object1 is less than object2"
        else:
            return "object2 is less than object1"
obj1 = a(35)
obj2 = a(5)
print(obj1 < obj2)