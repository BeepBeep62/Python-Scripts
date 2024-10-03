# Write a program to select a ride according to your preference. The ride is divided into two major categories: 1. Bike 2. Car And further, bikes and cars are divided into 2 subcategories. To give the user better selection options.
print("select your ride..............................")
print("1. bike")
print("2. car")
choice = int(input("enter choice: "))
if choice==1:
    print("what type of bike")
    print("1. scooter")
    print("2. scooty")
    choise =int(input("enter choice: "))
    if choise==1:
        print("you have selected scooter")
    else:
         print("you have selected scooty")
elif choice==2:
    print("what type of car")
    print("1. van")
    print("2. XUV")
    choise =int(input("enter choice: "))
    if choise==1:
        print("you have selected van")
    else:
         print("you have selected XUV")

else:
    print("invalid choice")