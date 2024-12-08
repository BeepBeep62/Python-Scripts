# Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.
class computer:
    # ey this is a clas i DRANK AN 8BALL OF  COKE AND  NOW I M ARVWRETVHCEHD ZAND OBROKE
    def __init__(self):
        self.__maxprice = 1000
    def sell(self):
        print("selling porice === ",self.__maxprice)
    def changeprice(self, price):
        self.__maxprice = price
laptop = computer()
laptop.sell()
laptop.changeprice(9000000)
laptop.sell()