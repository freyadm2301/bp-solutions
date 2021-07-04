# opgave 1 Schrijf onderstaande functies. Elke functie heeft één parameter van het datatype String.
# Functie ‘tel_kleine_woorden’:geeft het aantal kleine woorden uit de string terug(een klein woord bestaat uit max 3 karakters)
# Functie ‘tel_getallen’:geeft het aantal getallen uit de string terug
def tel_aantal_cijfers(zin):
    aantal = 0
    woord_per_woord = zin.split(" ")
    for woord in woord_per_woord:
        if woord.isnumeric():
            aantal +=1
    return aantal
mijn_zin = "Er zitten 3 studenten in 1 klas"
aantal_klein = tel_aantal_cijfers(mijn_zin)
print("Het aantal getallen is {0}".format(aantal_klein))

def tel_kleine_woorden(zin):
    aantal = 0
    woord_per_woord = zin.split(" ")
    for woord in woord_per_woord:
        if len(woord) <= 3:
            aantal += 1
    return aantal

mijn_zin = "ik ga naar het bunkertje en trakteer 5 maal"
aantal_klein = tel_kleine_woorden(mijn_zin)
print("Het aantal kleine woorden is {0}".format(aantal_klein))


#opgave 2 Schrijf de functie‘genereer_nummerplaat’.Deze functie geeft een nummerplaat terug waarbij
#het eerste deel één cijfer is;
#het tweede deel 3 willekeurige hoofdletters zijn;
#het derde deel: en getal bestaande uit 3 cijfers.
#De verschillende delen worden door een ‘-‘ van elkaar gescheiden.
#Vraag vooraf aan de gebruiker hoeveel nummerplaten er moeten samengesteld worden.Roep vervolgens zoveel keren bovenstaande functie op.

import random
import string
def genereer_nummerplaat():
    eerste_deel = 0
    tweede_deel = ""
    derde_deel = 0

    eerste_deel = random.randint(0,9)
    for teller in range(0, 3):
        tweede_deel += random.choice(string.ascii_uppercase)
    derde_deel = random.randint(0,999)

    return "{0}-{1}-{2}".format(eerste_deel,tweede_deel,derde_deel)
aantal_maal = int(input("Hoeveel nummerplaten wil u genereren "))
for i in range(0,aantal_maal):
    print(genereer_nummerplaat())


#opgave 3 Schrijf een functie ‘is_correct_paswoord’ met één string-parameter dieeen kandidaat-paswoord voorstelt. Deze functie controleert of het paswoord aan volgende voorwaarden voldoeten geeft nadien True (indien aan alle voorwaarden voldaan is) of False (in het andere geval) terug:
# 1.Minimum één letter tussen [a-z]
# 2.Minimum één cijfer tussen [0-9]
# 3.Minimum één letter tussen [A-Z]
# 4.Minimum één karakter uit [$#@]
# 5.Minimum lengte van 10 karakters
# 6.Maximum lengte van 18 karakters
import re
def is_correct_paswoord(kandidaat):
    if 10 <= len(kandidaat) <= 18:
        #ok
        if not re.search("[a-z]",kandidaat):
            #als geen enkel karakter dat is
            return False
        elif not re.search("[0-9]",kandidaat):
            return False
        elif not re.search("[A-Z]",kandidaat):
            return False
        elif not re.search("[$@#()!]",kandidaat):
            return False
        else:
            return True #ik ben op het einde gekomen dus het is correct
    else:
        #niet ok
        return False

if is_correct_paswoord("A2ERTYazER$Y") == True:
    print("correct paswoord")
else:
    print("foutief paswoord")