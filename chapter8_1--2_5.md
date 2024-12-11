# 1
## a)
### Vad är syntax errors?
Det är fel i programkoden, alltså motsatsen till att inhämtad / hanterad data är fel

## b)
### Varför skulle man vilja fånga exceptions i ett program och inte bara låta programmet stanna vid fel?
Om ett program körs flera gånger under obevakad tid, t ex under natten och ett fel uppstår under denna tid, som inte innebär att resten av processen MÅSTE avstanna, så är det bättre om man bara loggar felet och kör nästa.

## c)
### Varför skulle man vilja lyfta exceptions i ett program?
För att logga och / eller informera en användare om vad och att något gått fel eller om ngt i operationen inte går som man hade tänkt sig, vilket inte növändigtvis måste vara ett programmatiskt fel.

# 2
## a
### Förklara vad nedanstående kod gör.
`
def convert_string_to_int(string):
    try:
        int(string)
    except ValueError:
        return "Invalid input, cannot convert to integer."
    else:
        return int(string)

print(convert_string_to_int("314"))
print(convert_string_to_int("abc"))
`
Först försöker funktionen göra om en inkommande variabel, som ser ut att vara en sträng, till integer.
Om det inte lyckas så leverar funktionen en sträng enligt ovan.
Om det går så leveras inkommande variabel string som integer

## b)
### Generellt sett, vad är poängen med att använda else?
Detta avsnitt körs om try: INTE levererar en exception

# 5
### Din kollega, som är en skicklig programmerare, brukar innan hon försöker göra ett perfekt fungerande program testa olika ideér för att undersöka och lära sig mer om det problem hon försöker lösa. Nedan ser du ett av hennes skript som gjorts i syfte att undersöka och lära sig mer. Förklara vad det är hon gjort.
`
# Checking which exception is raised
try:
    5 + "Python is fun!"
except Exception as exception_instance:
    print(type(exception_instance))
    print(exception_instance)
`
## Här testar hon vilken exception som lyfts
Det kommer bli TypeError

`
# Checking which exception is raised
try:
    5/0
except Exception as exception_instance:
    print(type(exception_instance))
    print(exception_instance)
`
## Här testar hon vilken exception som lyfts
Det kommer bli DivisionByZero

`
def add_two_numbers(a, b):
    try:
        return(a/b)
    except TypeError:
        print("Both arguments must be numbers.")
    except ZeroDivisionError:
        print("Division by zero is not defined.")

# Testing so the functionality is as expected
print(add_two_numbers(5, 2))
print(add_two_numbers(5, "hello"))
print(add_two_numbers(5, 0))
`
## Här testar hon vilken exception som lyfts
I första altenativet blir det ingen excpetion alls som lyfts
I andra alternativet blir det ett TypeError
I tredje alternativet blir det ett DivisionByZero