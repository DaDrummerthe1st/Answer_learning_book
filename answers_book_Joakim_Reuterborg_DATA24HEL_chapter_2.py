# 1.
print('Add the two numbers'
    'num_1 = 5'
    'num_2 = 3'
    'in a variable called my_result')

num_1 = 5
num_2 = 3
my_result = num_1 + num_2
print(my_result)

# 2.
print('\n')
print('2. Multiplicera de två talen nedan och spara resultatet i en variabel som heter my_mult_result.'
    'Printa ut variabeln my_mult_-'
    'result.'
    'number_1 = 10'
    'number_2 = 7')
number_1 = 10
number_2 = 7
my_mult_result = number_1 * number_2
print(my_mult_result)

# 3.
print('\n')
print('3. Förklara vad nedanstående kod gör.'
      '10 % 3')
print('it finds the reminder (what is left over when divission is made after the integer is presented)')
print('result is: ',
      10%3)

# 4.
print('\n')
print('4. Vi vet att 27/6 = 4.5. Förklara vad nedanstående kod gör.'
    '27//6')
print('it divides 27 by 6')
print('Result is: '
      '27//6')

# 5.
print('\n')
print('5. Vad är fel i nedanstående kod? Rätta till koden så det fungerar.')
print("print('it's fun to learn Python!')")
print("""print('it\\'s fun to learn Python!')""")

# 6.
print('\n')
print("""6. Vad gör nedanstående kod? \n print("ha"*3)')""")
print('it prints the word ha three times, like so: ')
print('ha' * 3)

# 7.
print('\n')
print('7. Extrahera namnet “Anna” från strängen nedan genom att göra'
    'en slice. full_name = "Anna Andersson"')

full_name = "Anna Andersson"
print(full_name[0:5])
print(full_name.split())
name_list = full_name.split(' ')
print(name_list[0])

# 8.
print('\n')
print("""
    8. Hur många tecken har strängen nedan? Använd len()-
    funktionen.
    full_name = "Anna Andersson"
""")
full_name = "Anna Andersson"
print(len(full_name))

# 9.
print('\n')
print("""
        9.
    a) Genom att använda en f-string med de två variablerna founder
    och language, printa ut texten “Hello Guido, Python is really
    fun to learn!”
    b) Du vill nu skriva ut hela namnet “Guido van Rossum” så texten
    blir “Hello Guido van Rossum, Python is really fun to learn!”.
    Gör det genom att ändra namnet i variabeln founder och exe-
    kvera din f-string på nytt.
    founder = "Guido"
    language = "Python"
""")

class TextAnswer:
    """
    Takes two argument (founder, language)

    The method print_it() takes these two arguments and prints the sentence:
    Hello {founder}, {language} is really fun to learn!
    """
    def __init__(self, *, founder, language):
        self.founder = founder
        self.language = language

    def print_it(self):
        whole_sentence = f'Hello {self.founder}, {self.language} is really fun to learn!'
        print(whole_sentence)
        return whole_sentence

nine_a = TextAnswer(founder = "Guido", language = "Python").print_it()
nine_b = TextAnswer(founder = "Guido van Rossum", language = "Python").print_it()

# 10.
print('\n')
print("""
    10. Varför blir koden nedan fel?
    my_first_tuple = (10, 5, 'hi', 3)
    my_first_tuple[1] = 10
""")
print('Tuples är imutable')

# 11
print('\n')
print("""
    11. Vad gör koden nedan?
    my_tuple = ('languages', ['Python', 'Java', 'C', 'R'],'apples')
    print(my_tuple[0]) # languages
    print(my_tuple[-1]) # apples
    print(my_tuple[1][2]) # C
""")
print('skriver ut enligt ovan kommentarer')

# 12
print('\n')
print("""
12. Kolla på vilken datatyp variabeln my_tuple har genom att an-
vända type()-funktionen.
my_tuple = ('languages', ['Python', 'Java', 'C', 'R'],'apples')
""")
print('print(type(my_tuple))')
my_tuple = ('languages', ['Python', 'Java', 'C', 'R'],'apples')
print(type(my_tuple))

# 13
print('\n')
print("""
13. Vad gör koden nedan?
my_first_list = [10, 5, 'hi', 3]
my_first_list[1] = 7
my_first_list
""")
print('lägger till ett object ytterligare i listen och sen är det oklart, om det inte är i Jupyter,'
      'då är det jämställt med print()')

# 14
print('\n')
print("""
14. Se vilken datatyp variabeln my_first_list har genom att an-
vända type()-funktionen.
my_first_list = [10, 5, 'hi', 3]
""")

my_first_list = [10, 5, 'hi', 3]
print('print(type(my_first_list))')
print(type(my_first_list))

# 15
print('\n')
print("""
15. Beräkna antalet element i variabeln shopping_list genom att
använda len()-funktionen.
shopping_list = ['apple', 'banana', 'grapes', 'eggs','milk']
""")

shopping_list = ['apple', 'banana', 'grapes', 'eggs','milk']
print('print(len(shopping_list))')
print(len(shopping_list))

# 16
print('\n')
print("""
16. Vi glömde att lägga till bröd (bread på engelska) i vår shoppinglista. Gör det genom att använda
append()-metoden och printa ut den nya shoppinglistan.
shopping_list = ['apple', 'banana', 'grapes', 'eggs', 'milk']
""")

shopping_list = ['apple', 'banana', 'grapes', 'eggs', 'milk']
print("""
shopping_list.append('bread')
print(shopping_list)
""")
shopping_list.append('bread')
print(shopping_list)

# 17
print('\n')
print("""
17. Beräkna antalet gånger siffran 7 finns i listan my_numbers. Använd count()-metoden.
my_numbers = [1, 7, 2, 7, 10, 7]
""")

my_numbers = [1, 7, 2, 7, 10, 7]
print('print(my_numbers.count(7))')
print(my_numbers.count(7))


# 18
print('\n')
print("""
18. Konvertera one_tuple till en lista och spara det i en variabel som heter one_list.
one_tuple = (10, 5, 3)
""")
one_tuple = (10, 5, 3)
print("""
one_list = list(one_tuple)
print(type(one_list))
""")
one_list = list(one_tuple)
print(type(one_list))


# 19
print('\n')
print("""
19. Vad gör nedanstående kod?
my_first_dict = {'Anna': 38, 'Goran': 19, 'Lennart':59, 'Halimah': 28}
my_first_dict['Goran']
""")

print('i Jupyter visas "19". Den sista raden tar fram nyckeln "Goran"')

# 20
print('\n')
print("""
20. Kolla på vilken datatyp variabeln my_first_dict har genom att
använda type()-funktionen.
""")
my_first_dict = {'Anna': 38, 'Goran': 19, 'Lennart':59, 'Halimah': 28}
print('print(type(my_first_dict))')
print(type(my_first_dict))

# 21
print('\n')
print("""
21. Varför printas elementet 5 endast ut en gång i koden nedan?
my_set = {10, 5, 2, 5, 5}
print(my_set)
{10, 2, 5}
""")

print('sets are considered only containing unique elements')

# 22
print('\n')
print("""
22. Vi har definierat de två mängderna A och B nedan.
a) Hitta alla element som är i både A och B. Använd intersection()-metoden.
66b) Hitta alla element som är i A och/eller B. Använd union()-metoden.

c) Hitta alla element som är i A men inte i B. Använd difference()-metoden.
A = {1, 2, 3, 4, 5}
B = {3, 10, 5, 7}
""")

A = {1, 2, 3, 4, 5}
B = {3, 10, 5, 7}
print('22.a: ', A.intersection(B))
print('22.b ', A.difference(B))

# 23
print('\n')
print("""
23. Vi har definierat de två listorna list_a och list_b nedan.
Nedanstående uppgifter kan enkelt lösas genom att konvertera
de definierade listorna till mängder först.
list_a = [1, 2, 3, 4, 5]
list_b = [5, 6, 10, 21]
a) Hitta alla element som är i både list_a och list_b.
b) Hitta alla element som är i list_a och/eller list_b.
""")

list_a = [1, 2, 3, 4, 5]
list_b = [5, 6, 10, 21]
print('23.a ', set(list_a).intersection(set(list_b)))
print('23.b ', set(list_a).union(set(list_b)))

# 24
print('\n')
print("""
24. Hitta alla unika element i variabeln duplicate_values genom att konvertera tuple:n till ett set.
duplicate_values = (10, 2, 2, 10, 1)
""")

duplicate_values = (10, 2, 2, 10, 1)
print(set(duplicate_values))
