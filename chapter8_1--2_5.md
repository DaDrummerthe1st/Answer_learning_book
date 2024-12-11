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