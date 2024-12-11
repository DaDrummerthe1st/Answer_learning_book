# Gör klasser som UML-diagram för att börja träna på det
from fileinput import hook_encoded

from runpy import run_module

# 1
print('\n')
print("""
1. Kolla vilka klasser variablerna a, b, c, och d tillhör genom att an-
vända type()-funktionen. Notera att vi i variabeln d har sparat
en funktion. Vi hade kunnat anropa den genom att till exempel
skriva d(2).
a = 10
b = [5, 7, 3]
c = {2, 7, 1, 8, 2, 8}
def my_fun(x):
return 2*2
d = my_fun
""")
a = 10
b = [5, 7, 3]
c = {2, 7, 1, 8, 2, 8}
def my_fun(x):
    return 2*2
d = my_fun

print(type(a))
print(type(b))
print(type(c))
print(d('w'))

# 2
print('\n')
print("""
2.
a) Kolla om variabeln my_variable är en instans av tuple-klassen
genom att använda isinstance()-funktionen.
b) Kolla om variabeln my_variable är en instans av list-klassen
genom att använda isinstance()-funktionen.
my_variable = (1, 1, 2, 3, 5)
""")
my_variable = (1, 1, 2, 3, 5)

if isinstance(my_variable, tuple):
    print("Is tuple")
elif isinstance(my_variable, list):
    print("is list")

# 3
print('\n')
print("""
3. I denna uppgiften skall du göra följande:
a) Skapa en klass som heter FruitProduct som har en docstring
där det står “A class representing fruit products in a grocery
store”.
b) Klassen skall ha instans-attributen price och quantity. Detta
gör du i samband med __init__().
c) Instantiera klassen och spara instansen i variabeln swedish_apples.
Dess pris skall vara 52 och dess kvantitet 1. Det är
underförstått att vi menar kronor respektive kg.
d) Printa ut klassens docstring genom att använda dig av __doc__.
e) Printa ut attributen från swedish_apples-instansen.
f) Kolla vilken klass instansen swedish_apples tillhör genom att
använda type()-metoden.
g) Kolla om swedish_apples tillhör klassen FruitProduct genom
att använda isinstance()-metoden.
""")

print('Uppgift 3.a, 3.b:')
class FruitProduct:
    """A class representing fruit products in a grocery store"""
    def __init__(self, price, quantity):
        self.price = price # in SEK
        self.quantity = quantity # in kilogram (kg)

    def print_attributes_and_values(self, ):
        """Displays values for attributes in self"""
        pass

print('Uppgift 3.c')
swedish_apples = FruitProduct(price=52, quantity=1)

print('Uppgift 3.d')
print(swedish_apples.__doc__)

print('Uppgift 3.e')

# I chose to interpret the task literally ANd develop beyond that.
# Thus, my solution both contains finding the different attributes
# and thereafter getting their values
# This is what I display basically:
# print(swedish_apples.__dir__()[0:2])

index = 0
for index, attribute in enumerate(swedish_apples.__dir__()):
    if index <= 1:
        print(f'{attribute}')
        # attribute = 'swedish_apples.' + attribute
        print(f'{getattr(swedish_apples, attribute)}')
        index += 1

print('Uppgift 3.f')
print(type(swedish_apples))

print('Uppgift 3.g')
if isinstance(swedish_apples, FruitProduct):
    print('swedish_apples is an instance of FruitProduct')

# 4
print('\n')
print("""
4. Skapa en klass Square vars instanser har attributet side_length.

Skapa två metoder, perimeter() och area() där metoderna beräknar omkretsen
respektive arean givet längden på kvadraternas sidor som finns i attributet
side_length.

Skapa en instans my_square med sidlängden 8. Beräkna omkretsen och arean av
my_square genom att använda de två metoderna som du har skapat.
""")

class Square:
    """does calculations on a square given side_length"""
    def __init__(self, side_length):
        self.side_length = side_length

    def perimeter(self):
        """calculates perimeter b using side_length"""
        return self.side_length*4

    def area(self):
        """Calculates the area by using side_length"""
        return self.side_length**2

hip_2_b_square = Square(8)
print(hip_2_b_square.perimeter())
print(hip_2_b_square.area())

# 5
print('\n')
print("""
5.
a) Förklara vad nedanstående kod gör.

b) Prova att ändra variabeln L i koden nedan till en tuple och se
vad som sker när du kör om all kod.
""")

# TODO what happens if the class is written with parentheses? What is that used for?
class DescriptiveStatistics:
    """This class provides functionality for calculating descriptive
    statistics from a list."""

    def __init__(self):
        self.data = []

    def add_data(self, data):
        if isinstance(data, list):
            self.data.extend(data)
        else:
            """Code below raises an error if the data is not a list. 
            Will be covered in chapter 8 of the book.
            raise Exception('Only "Lists" are accepted as data.')"""

    def calc_sum(self):
        return sum(self.data)

    def calc_nbr_of_elements(self):
        return len(self.data)

    def calc_mean(self):
        return (self.calc_sum()) / (self.calc_nbr_of_elements())

    def print_summary(self):
        print('Sum:', self.calc_sum())
        print('Number of elements:', self.calc_nbr_of_elements())
        print('Mean:', self.calc_mean())

L = [1, 2, 1, 3, 5, 7, 4, 9, 10, 3, 2, 1, 6, 4, 3, 2, 1, 10, 9, 1, 8, 7, 3, 2, 1]
my_data = DescriptiveStatistics()
my_data.add_data(L)

print(my_data.data)

print('Sum:', my_data.calc_sum())
print('Number of elements:', my_data.calc_nbr_of_elements())
print('Mean:', my_data.calc_mean())

my_data.print_summary()

print("""
5.a
A class is built to handle a list of numbers (int/float)
In the class the different methods does the following:
add_data: setter_method to inserts data into the instance attribute list "data"
   - it can only handle lists!
calc_sum returns the sum of all the elements on the first level in the list
calc_num_of_elements returns the amount of elements on the first dimension of the list
calc_mean returns the mean value of all the elements on the first level of the list
print_summary prints all the above methods returns with some added explanation
L is a list
my_data = DescriptiveStatistics instantiates the class DescriptiveStatistics
my_data.add_data(L) sets the list L as input in the setter method of the instance my_data
print(my_data.data) prints the just inserted list
these three lines does exactly the same as the print_summary-method does
again, prints summary
""")
print("""
5.b instantierar igen men med en tuple istället
""")
# TODO ignore instance usage when self.data != single dimension list of only ints and floats
# print('I rewrite the class to handle the Exception')
#
# class DescriptiveStatistics:
#     """This class provides functionality for calculating descriptive
#     statistics from a list."""
#
#     def __init__(self):
#         self.data = []
#
#     def add_data(self, data):
#         print(f"{self.data} is whatcha want. right?")
#         try:
#             if isinstance(data, list):
#                 self.data.extend(data)
#         except:
#             """Code below raises an error if the data is not a list.
#             Will be covered in chapter 8 of the book.
#             raise Exception('Only "Lists" are accepted as data.')"""
#             print(f'{self.data} is not of type list. Exiting')
#
#     def calc_sum(self):
#         return sum(self.data)
#
#     def calc_nbr_of_elements(self):
#         return len(self.data)
#
#     def calc_mean(self):
#         return (self.calc_sum()) / (self.calc_nbr_of_elements())
#
#     def print_summary(self):
#         print('Sum:', self.calc_sum())
#         print('Number of elements:', self.calc_nbr_of_elements())
#         print('Mean:', self.calc_mean())
#
# t = (1, 2, 1, 3, 5, 7, 4, 9, 10, 3, 2, 1, 6, 4, 3, 2, 1, 10, 9, 1, 8, 7, 3, 2, 1)
# my_data2 = DescriptiveStatistics()
# my_data2.add_data(t)
#
# print(my_data2)
# my_data2.print_summary()

# # 7
# print('\n')
# print("""
# 7. Din kollega Adrian frågar dig, vad är klasser för något? Försök
# förklara detta för Adrian. Använd begreppen instanser, attribut
# samt metoder i din förklaring.
# """)
