# 1
print('\n')
print("""
1. Printa ut alla element i listan looping_list med en for-loop.
looping_list = [0, 'a', 'b', [1, 2, 3], ('Python', 'R','C', 'Java'), 55]
""")
looping_list = [0, 'a', 'b', [1, 2, 3], ('Python', 'R','C', 'Java'), 55]
for thing in looping_list:
# TODO
#    if type(thing) != (int, str):
#        print('yes')
#      for thing_lvl2 in thing:
#           print(thing_lvl2)
#            continue
    print(thing)

# 2
print('\n')
print("""
2. Printa ut alla element i listan looping_list med en for-loop.
Printa även ut vilken iteration det är genom att använda funk-
tionen enumerate().
looping_list = [0, 'a', 'b', [1, 2, 3], ('Python', 'R',
↪
'C', 'Java'), 55]
""")
looping_list = [0, 'a', 'b', [1, 2, 3], ('Python', 'R', 'C', 'Java'), 55]
for index, value in enumerate(looping_list):
    print(index, value)

# 3
print('\n')
print("""
3. Printa ut talen 0, 5, 10, 15, 20 med en for-loop där du använder
range()-funktionen.
""")
for number in range(0,21):
    if number % 5 == 0:
        print(number)

# 4
print('\n')
print("""
4. Skriv en for-loop för att printa ut varje bokstav separat i variabeln for_string.
for_string = 'Python!'
""")
for_string = 'Python!'
for char in for_string:
    print(char)

# 5
print('\n')
print("""
5. Skriv en while-loop för att printa ut varje bokstav separat i
variabeln while_string.
while_string = 'Is Awesome!'
""")
while_string = 'Is Awesome!'
i = 0
while i < len(while_string):
     print(while_string[i])
     i += 1



# 6
print('\n')
print("""
6. Printa ut talen 1, 2, 3, …, 10 med en while-loop.
""")
i = 1
while i < 11:
    print(i)
    i += 1

# 7
print('\n')
print("""
7. Printa ut alla tal som är delbara med 5 i listan som är sparad
i variabeln numbers. För att se om ett tal är delbart med 5 så
kan du använda modulo-operatorn %. Ett tal är delbart med 5
om dess rest är 0 när det delas med 5.
numbers = [10, 20, 34, 46, 55]
""")
numbers = [10, 20, 34, 46, 55]
for number in numbers:
    if number % 5 == 0:
        print(number)

# 8
print('\n')
print("""
8. Förklara vad nedanstående kod gör.
my_list = []
for i in range(10):
    if i % 2 == 0:
        my_list.append(i)
print(my_list)
""")

print('en tom lista skapas: my_list'
      'for-satsen körs 10 gånger'
      'om det är ett jämnt tal eller talet noll'
      'läggs detta till i my_list'
      'när for-satsen körts klart skrivs hela listan ut')
my_list = []
for i in range(10):
    if i % 2 == 0:
        my_list.append(i)
print(my_list)

# 9
print('\n')
print("""
9. Använd en for-loop för att skapa en ny lista från list_example,
där varje tal är multiplicerat med 10. Du skall endast inkludera
talen mellan 4-8 där 4 och 8 är inkluderat från list_example.
list_example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
""")

list_example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for place, instance in enumerate(list_example):
    if 4 <= instance <= 8:
        list_example[place] = instance * 10
print(list_example)

# 10
print('\n')
print("""
10. Förklara vad nedanstående kod gör.
for i in range(100):
    if i in (5, 7, 8):
        continue
    if i > 10:
        break
    print(i)
else:
    print('We are done!')
""")

print('for-satsen initieras med att räkna mellan 0 - 99'
      'om variabeln i är 5, 7 eller 8'
      'gå till nästa iteration i for-loopen (if i > 10:)'
      'men är det inte 5, 7 eller 8 men större än 10'
      'avbryt hela operationen'
      ''
      'Det betyder i praktiken att endast siffrorna 0 -- 4, 6, 9, 10 kommer att skrivas ut'
      'följt av meddelandet "We are done!')

for i in range(100):
    if i in (5, 7, 8):
        continue
    if i > 10:
        break
    print(i)
else:
    print('We are done!')