# Write a program to create two classes for two different countries that consist of three methods to display the following information of respective country - capital, language and type of country. Then, use Polymorphism to create a common interface for both classes.
class america():
    def capotal(self):
        print("washington dc")
    def language(self):
        print("english")
    def type(self):
        print("developcountry")
class pakistan():
    def capotal(self):
        print("islamabad")
    def language(self):
        print("urdu")
    def type(self):
        print("developingcountry")
of = america()
op = pakistan()
op.capotal()
op.language()
op.type()
of.capotal()
of.language()
of.type()
for country in (of, op):
    country.capotal()
    country.language()
    country.type()
    