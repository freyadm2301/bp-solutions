# opgave 1 Schrijf onderstaande functies. Elke functie heeft één parameter van het datatype String.
# Functie ‘tel_kleine_woorden’:geeft het aantal kleine woorden uit de string terug(een klein woord bestaat uit max 3 karakters)
# Functie ‘tel_getallen’:geeft het aantal getallen uit de string terug

def tel_kleine_woorden(zin):
    kleine_woorden = 0
    lijst_met_woorden = zin.split(" ")
    for woord in lijst_met_woorden:
       if woord.isalpha() and len(woord) <= 3:
           kleine_woorden += 1

    aantal_kleine_woorden = print("Het aantal kleine woorden in deze zin is: {0}".format(kleine_woorden))
    return aantal_kleine_woorden

def tel_getallen(zin):
    getelde_getallen = 0
    opgesplitste_zin = zin.split(" ")
    for element in opgesplitste_zin:
        if element.isnumeric():
            getelde_getallen += 1

    aantal_getallen = print("Het aantal getallen in deze zin is: {0}".format(getelde_getallen))
    return aantal_getallen

zin = input("Welke zin moet onderzocht worden? ")
tel_kleine_woorden(zin)
tel_getallen(zin)


#opgave 2 Schrijf de functie‘genereer_nummerplaat’.Deze functie geeft een nummerplaat terug waarbij
#het eerste deel één cijfer is;
#het tweede deel 3 willekeurige hoofdletters zijn;
#het derde deel: en getal bestaande uit 3 cijfers.
#De verschillende delen worden door een ‘-‘ van elkaar gescheiden.
#Vraag vooraf aan de gebruiker hoeveel nummerplaten er moeten samengesteld worden.Roep vervolgens zoveel keren bovenstaande functie op.

import random
import string

def genereer_nummerplaat(invoer_gebruiker):
    plaatn = 0
    while plaatn < invoer_gebruiker :
        deel1 = random.randint(0,9)

        deel2 = ""
        for teller in range(0, 3):
            deel2 += random.choice(string.ascii_uppercase)

        deel3 = ""
        for teller in range(0, 3):
            deel3 += random.choice(string.digits)

        plaatn += 1
        print("Nummerplaat {0}: {1}-{2}-{3}".format(plaatn,deel1,deel2,deel3))


invoer_gebruiker = int(input("Hoeveel nummerplaten wenst u? "))
genereer_nummerplaat(invoer_gebruiker)


#opgave 3 Schrijf een functie ‘is_correct_paswoord’ met één string-parameter dieeen kandidaat-paswoord voorstelt. Deze functie controleert of het paswoord aan volgende voorwaarden voldoeten geeft nadien True (indien aan alle voorwaarden voldaan is) of False (in het andere geval) terug:
# 1.Minimum één letter tussen [a-z]
# 2.Minimum één cijfer tussen [0-9]
# 3.Minimum één letter tussen [A-Z]
# 4.Minimum één karakter uit [$#@]
# 5.Minimum lengte van 10 karakters
# 6.Maximum lengte van 18 karakters

lowerc = "abcdefghijklmnopqrstuvwxyz"
lowercase = list(lowerc)
uppercase = list(lowerc.upper())
nummers = "0123456789"
digits = list(nummers)
karakter = "$#@"
punctuation = list(karakter)
def is_correct_paswoord(opgegeven_paswoord):
    aantal_klein = 0
    aantal_groot = 0
    aantal_nummer = 0
    aantal_karakt = 0
    if 10 <= len(opgegeven_paswoord) <= 18:
         for element in opgegeven_paswoord:
             if element in lowercase:
                aantal_klein += 1
         for element in opgegeven_paswoord:
             if element in uppercase:
                aantal_groot += 1
         for element in opgegeven_paswoord:
             if element in digits:
                aantal_nummer += 1
         for element in opgegeven_paswoord:
             if element in karakter:
                aantal_karakt += 1
        
         if aantal_klein != 0 and aantal_groot != 0 and aantal_nummer != 0 and aantal_karakt != 0 :
             uitkomst = True
         else:
            uitkomst = False

    else:
       uitkomst = False
    return uitkomst

opgegeven_paswoord = input("Geef uw paswoord: ")
print("{0} -> Geldig paswoord? {1}".format(opgegeven_paswoord,is_correct_paswoord(opgegeven_paswoord)))