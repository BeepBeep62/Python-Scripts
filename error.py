# Write a program to check how the exceptions and finally statement works, what happens when you name a file .py? that's the question,
try:
    n1 = int(input("enter first number: "))
    n2 = int(input("ennter second number:.."))
    resultt = n1/n2
except SyntaxError:
    print("THERE%%%^^ A SYNTA%^ ERROR ^_^")
except ZeroDivisionError:
    print("THERE%%%^D::: DDDDD: :000 :< /:I^ A zero divisoon ERROR R%^ ERROR ^_^")
except TypeError:
    print("THERE%%%^^ A TYPE ERROR 0101010100101%^ ERROR TYPEMT TIPE ^_^")
except:
    print("THERES AN ERROR !&^££££££££££££££££££ &7 I DON KNOWZ8 WHICH ONE ^_^")
finally:
    print("understandable, have a nice day.")
