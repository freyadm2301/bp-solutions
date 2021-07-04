# Maak een Python programma dat de leeftijd van een hond vertaalt naar een overeenkomstige leeftijd van een mens. Vraag eerst aan de gebruiker de leeftijd van zijn hond. Nadien print je een correcte boodschap af waarbij:
# - Indien getal < 0, geef een foutmelding terug.
# - Indien leeftijd = 1 -> 14 mensenjaren
# - Indien leeftijd = 2 -> 22 mensenjaren
# - Indien meer dan 2: mensenleeftijd = 22 + (jaren –2) * 5

leeftijd = int(input("Geef de leeftijd op van uw hond: "))

if leeftijd < 0:
    print("ERROR")
elif leeftijd == 1:
    print("Deze leeftijd komt overeen met 14 mensenjaren.")
elif leeftijd == 2:
    print("Deze leeftijd komt overeen met 22 mensenjaren.")
elif leeftijd > 2:
    mensenjaren = 22 + (leeftijd - 2) * 5
    print("Deze leeftijd komt overeen met {0} mensenjaren.".format(mensenjaren))