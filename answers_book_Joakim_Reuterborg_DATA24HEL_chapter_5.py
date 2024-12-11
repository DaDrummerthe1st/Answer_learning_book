# 1 2
print('\n')
print("""
1. Vad är funktioner för något?
2. Vad är parametrar och argument för något?
""")
def answer_to_both_one_two(functionparameter, parameter):
    return f'{functionparameter} är skissen på en process i vilken man kan ta emot {parameter}.'
print(answer_to_both_one_two('Funktion', 'argument'))

# 3
print('\n')
print("""
3. Skapa en funktion som heter uppercase_converter. Funktio-
nen skall ta en sträng som ett argument och returnera strängen
med stora bokstäver (versaler). Exempel: uppercase_conver-
ter("hello") skall returnera “HELLO”.
""")

def uppercase_converter(input_string):
    return f'{input_string.upper()}'

print(uppercase_converter('hej hej'))

# 4
print('\n')
print("""
4. Skapa en funktion add_subtract_function som tar två argu-
ment och som returnerar både summan och subtraktionen av
de två talen i en tuple. Funktionen skall alltså returnera två
resultat.
""")
def add_subtract_function(a, b):
    sum = a + b
    subtraction = a -b
    return (sum, subtraction)
print(add_subtract_function(7, 3))

# 5
print('\n')
print("""
5. Skapa en funktion som innehåller minst en “endast-
positionsparameter”, minst en “positions-eller-nyckelordsparameter”
samt minst en “endast-nyckelordsparameter”.
Ledning: f(pos_only, /, pos_or_kwd, *, kwd_only).
""")
def add_subtract(a, /, b, *, c):
    sum = a + b + c
    sub = a - b - c
    return sum, sub

print(add_subtract(1, b = 2, c = 3))
print(add_subtract(4, 5, c = 6))

# 6
print('\n')
print("""
6. Förklara vad nedanstående kod gör.
def my_sum_function(x1, x2):
return x1 + x2
a = my_sum_function
a(1, 2)
""")
print('levererar resultatet 3')
def my_sum_function(x1, x2):
    return x1 + x2

a = my_sum_function
print(a(1, 2))

# 7
print('\n')
print("""
7. Skriv en funktion som du kallar för add_or_multiply. Funktio-
nen add_or_multiply skall ta tre argument. De första två är
tal, medan det tredje specificierar huruvida du önskar addera
eller multiplicera de två talen. Om användaren av funktionen
varken specificerar add eller multiply som det tredje argumen-
tet så skall meddelandet "Choose either add or multiply."
printas ut.
Exempel:
add_or_multiply(2, 5, "add") = 7
add_or_multiply(2, 5, "multiply") = 10
add_or_multiply(2, 5, "Wrong") skall printa ut meddelandet:
Choose either "add" or "multiply".
""")
def add_or_multiply(a, b, func):
    calc = 0
    # a = input("Write an integer")
    if type(a) != int:
        print(f"{a} är inte en integer!")
    # print((type(a), type(b), type(func)))
    if type(b) != int:
        print(f"{b} är inte en integer!")
    if str(func) == 'add':
        calc = a + b
    elif str(func) == 'multiply':
        calc = a * b
    else:
        print(f"{func} is not an operator! Choose either \"add\" or \"multiply\".")

    return calc


print(add_or_multiply(3, 4,'tisdag'))

# 8
print('\n')
print("""
8. Kör koden nedan och förklara vad som sker.
name = input('What is your name dear stranger?')
print("Mom, I met a person who's name is:", name)
""")
name = input('What is your name dear stranger?')
print("Mom, I met a person who's name is:", name)

print(f"Den tar name {name} från user interaction och sätter in i en print")