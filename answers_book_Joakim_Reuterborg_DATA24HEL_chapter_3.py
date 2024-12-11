# 1
print('\n')
print("""
1. Förklara vad nedanstående kod gör.
age = 23
if age > 18:
    print('You can take a drivers license')
else:
    print('You are too young to take a drivers license')
""")

print('Först ges variabeln age värdet 23 '
      'därefter kontrolleras om age är högre än 18 '
      'Om det är det, vilket stämmer i detta fall, så printas "You can take a drivers license" till konsollen '
      'annars (används inte eftersom if-statemeneten stämde) '
      'skrivs You are to youn to take a drivers license')
age = 23
if age > 18:
    print('You can take a drivers license')
else:
    print('You are too young to take a drivers license')

# 2
print('\n')
print("""
2. Skapa ett program som undersöker om värdet i variabeln x ne-
dan är större än 10, mellan 10 och 5, eller mindre än 5 där
någon text printas ut för varje av de tre fallen som undersöks.
x = 7
""")
x = 7
if x > 10:
    print('x är större än 10')
elif 10 >= x >= 5:
    print('talet är mellan 10 och 5')
elif x < 5: # else: hade också fungerat eftersom ovan är uttömmande
    print('talet är lägre än 5')

# 3
print('\n')
print("""
3. Varför blir resultatet True när koden nedan exekveras?
1 == True
""")
print('För att 0 och 1 är detsamma som False och True')

# 4
print('\n')
print("""
4. Vad blir resultatet om nedanstående kod exekveras?
10 > 15
""")
print('Svaret blir False eftersom 10 är MINDRE ÄN 15')
print(10 > 15)

# 5
print('\n')
print("""
5. Vad blir resultatet om nedanstående kod exekveras?
7 >= 7
""")
print('svaret blir True eftersom 7 ÄR samma som 7')
print(7 >= 7)

# 6
print('\n')
print("""
6. Vad blir resultatet om nedanstående kod exekveras?
3 != 3
""")
print('False, för att 3 ÄR lika med 3')
print(3 != 3)

# 7
print('\n')
print("""
7. Vad blir resultatet om nedanstående kod exekveras?
5 >= 5 and 5 > 6
""")
print('False, eftersom 5 är lika men 5 är MINDRE än 6 ')
print(5 >= 5 and 5 > 6)

# 9
print('\n')
print("""
8. Vad blir resultatet om nedanstående kod exekveras?
5 >= 5 or 5 > 6
""")
print('True, eftersom 5 ÄR lika med 5, även om 5 är mindre än 6')
print(5 >= 5 or 5 > 6)

# 10
print('\n')
print("""
10. Förklara skillnaden mellan nedanstående två kodblock.
number = 8
if number < 5:
    print('Less than 5')
if number < 10:
    print('Less than 10')
if number < 100:
    print('Less than 100')
___
if number < 5:
    print('Less than 5')
elif number < 10:
    print('Less than 10')
elif number < 100:
    print('Less than 100')
""")
print('i den övre körs varje if-sats, i den undre itereras endast tills dess att ett svar är True.'
      'Den övre är 3 olika funktioner medan den undre är en sammansatt funktion')
number = 8
if number < 5:
    print('Less than 5')
if number < 10:
    print('Less than 10')
if number < 100:
    print('Less than 100')

if number < 5:
    print('Less than 5')
elif number < 10:
    print('Less than 10')
elif number < 100:
    print('Less than 100')