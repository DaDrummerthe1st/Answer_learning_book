# Uppgift 1
## a)
### Om du arbetar i ett projekt som har ett internt dokument med style guidelines där vissa saker går emot vad PEP 8 säger, vad gör du då?
Lokala guidelines finns ju av en anledning och skall därför betraktas som giltiga där konflikter uppstår

## b)
### På vilket språk skall kommentarer generellt sett skrivas?
Engelska, om man inte är 120% säker på att ingen från något annat språk kommer läsa det

## c)
### Hur skall funktioner och variabler namnges?
Båda ska skrivas på samma sätt med gemener. Ord eller vid behov annat, ska separeras med underscore

## d)
### Hur skall klasser namnges?
Som "CamelCase", dvs första bokstaven i varje nytt ord, inkl den första som versal och resten som gemener

## e)
### Om du i ditt skript importerar exempelvis en modul, var i skriptet skall koden som utför importen placeras?
Först, enligt denna sortering:
1. stanardbibliotek
2. Relaterade tredjepartsimporter
3. Lokala applikationer / bibliotek

## f)
### Enligt PEP 8, skall man använda enkla ('my_string') eller dubbla ("my_string") citationstecken för att skapa en sträng?
DOCSTRINGS ska inledas på samma rad som det första innehållet i DOCSTRINGEN med tre dubbla citattecken (""")och på en egen rad avslutas med tre dubbla citatectken (""") om inte allt står på samma rad:
"""DOCSTRING for module1
This Module creates a universe
"""

"""This is a docstring on a single row"

## g)
### Vilket av Alternativ 1 och Alternativ 2 nedan är det korrekta sättet att skriva koden på, enligt PEP 8?
`
# Alternativ 1
a1 = 5 + 2
# Alternativ 2
a2=5+2
`
Alternativ 1 är rätt. Mellanslag ska stå runtoperatorer. När operatorer av olika slag används så ska den operatorn med lägst prioritet få mellanslag.

# 2.
## a)
### “Explicit is better than implicit.” Vad tror du det innebär? Kan du exemplifiera?
Det är bättre att faktiskt uttrycka något tydligt än anta att läsaren (en annan programmerare) förstår det.
`
# This might be hard to undderstand wothout explanation
class FiNaR:

# While this is probably easier
class FirstNameReader:
`

## 2)
### “Simple is better than complex.” Vad tror du det innebär? Kan du exemplifiera?
Ju mer man förenklar och skriver sin kod intuitivt, desto lättare kommer den vara att förstå.
Mitt bästa exempel är nog hur PEP 8 är skriven - det mesta är intuitivt och tillser att få en readability

## 3
### “Det känns krångligt att vi alla skall behöva följa konventioner och standarder. Är det inte lättare om alla bara skriver kod på det sättet som de vill, så länge som den fungerar?” Vad svarar du?
Problemet när man inte håller sig till standarder är att det blir svårt för andra att övervaka och bidra. Min erfarenhet är att det också blir svårare att gå tillbaka ett långt tag efteråt till sin egen kod o förstå den eftersom konventionerna ofta består av väldigt lång erfarenhet av standarder som förenklar