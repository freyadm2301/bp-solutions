# Gebruik van controlestructuren

## Oef 1
Vraag twee getallen aan de gebruiker. Controleer of deze gelijk zijn aan elkaar of verschillend. Print een gepaste boodschap af.

## Oef 2
Vraag een niet-decimaal getal aan de gebruiker. Bepaal of het opgegeven getal even of oneven is. Print een gepaste boodschap af.

## Oef 3a
Vraag aan de gebruiker wat zijn geboortejaar is. Indien hij nog geen 18 is, print dan ook een gepaste melding af.
## Oef 3b
Hou ook rekening met de geboortemaand en geboortedag om te verifiëren of iemand reeds 18 is.

## Oef 4
Maak een Python programma dat de leeftijd van een hond vertaalt naar een overeenkomstige leeftijd van een mens. Vraag eerst aan de gebruiker de leeftijd van zijn hond. Nadien print je een correcte boodschap af waarbij:
- Indien getal < 0, geef een foutmelding terug.
- Indien leeftijd = 1 -> 14 mensenjaren
- Indien leeftijd = 2 -> 22 mensenjaren
- Indien meer dan 2: mensenleeftijd = 22 + (jaren –2) * 5

## Oef 5
Vraag de decimale score van een module aan de gebruiker. Print nadien af of hij/zij geslaagd is. Zorg ervoor dat de score correct afgerond wordt: indien het decimale gedeelte kleiner is dan 0,5 wordt er naar beneden afgerond. In het andere geval wordt er naar boven afgerond. Print ook de afgeronde score af.

## Oef 7
Vraag aan de gebruiker twee woorden op. Ga na of deze aan elkaar gelijk zijn (zonder rekening te houden met kleineletters of hoofdletters)

# Werken met functies
## Oef 8
Schrijf een functie ‘printWelkom’ die een string als parameter heeft. Deze string stelt de naam voor. Print in de functie een welkomsbericht af waarin de naam gebruikt wordt. Test de methode met verschillende namen.

## Oef 9
Schrijf een functie ‘printWelkom’ die twee strings als parameters heeft: naam en groep. Zorg ervoor dat de parametergroep een defaultwaarde ‘NMCT @ Athena’ krijgt. Print een welkomstbericht af waarin naam & groep vermeld staan. Test de functie voldoende (zowel met 1 als 2 argumenten)

## Oef 10
Schrijf een functiemet 4 parameters (a,b,c,d) die getallen voorstellen. De laatste 2 parameters hebben 0 als default-waarde. De functie geeft het resultaat van volgende berekening terug: a –b + c –d.
- Roep de functie aan door 4 getallen door te geven
- Roep de functie aan met dezelfde 4 getallen maar in andere volgorde (gebruik de parameternamen)
- Roep de functie aan met twee getallen

## Oef 11
Schrijf een functie die 3 getallen binnenkrijgt. De functie geeft het maximum terug.

## Oef 12
Schrijf een functie die een maandnummer binnenkrijgt. Controleer of het getal tussen 1 en 12 ligt. Geef de corresponderende maand terug. Indien buiten het interval, geef je een foutboodschap terug. Test de functie met meerdere maandnummers.

## Oef 13 
Schrijf volgende twee functies:
- Eerste functie:‘geef_celsius’ krijgt een temperatuur in Fahrenheit binnen. De overeenkomstige temperatuur in Celsius wordt berekend en teruggegeven.
De formule is: temp = (t_in_fahrenheit - 32) * 5 / 9
- Tweede functie:‘geef_fahrenheit’ krijgt een temperatuur in Celsius binnen. De overeenkomstige temperatuur in Fahrenheit wordt berekend en teruggegeven.
De formule is: temp = (temp_in_celsius * 9 / 5) + 32

Vraag aan de gebruiker welke temperatuureenheid hij gebruikt. Vraag vervolgens de temperatuur. Bereken de overeenkomstige temperatuur en print deze af.
