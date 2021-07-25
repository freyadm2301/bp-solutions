# Gegeven het bronbestand ‘spelers.txt’.
# Analyseer het bronbestand: elke regel bestaat uit de gegevens van een voetbalspeler.
# Maak een applicatie die het bronbestand inleest,
# en vervolgens 11 verschillende spelers willekeurig selecteert om als ploegopstelling te kunnen fungeren.
# Deze 11 spelers worden in een nieuw bestand weggeschreven.
# Bepaal vooraf welke datastructuur je zal gebruiken om alle data bij te houden.
# Werk vervolgens in deelproblemen door oa. gebruik te maken van onderstaande functies:
# - Functie ‘inlezen_spelers’ die het bronbestand correct inleest en data in een datastructuur bijhoudt
# - Functie ‘afprinten_spelers’ die in staat is om alle spelers uit de gekozen datastructuur af te printen
# - Functie  ‘selecteer_random_elftal’ die in staat is om 11 verschillende spelers te selecteren
# - Functie ‘opslaan_ploegopstelling’ die in staat is om een opstelling naar een tekstbestand weg te schrijven.
# Test voldoende uit.

import random
spelers = []

def inlezen_spelers(path):
    fo = open(path, 'r')
    lijn = fo.readline().rstrip('\n')
    lst_res = []
    while lijn != '':
        lst_res.append(lijn)
        lijn = fo.readline().rstrip('\n')
    fo.close()
    return lst_res

def afprinten_spelers(een_lijst):
    nummer = 1
    for naam in een_lijst:
        print('{0}: {1}'.format(nummer, naam))
        nummer += 1

def selecteer_random_elftal(een_lijst):
    selectie = []

    while len(selectie) < 11:
        gekozen_index = random.randint(0, len(een_lijst)-1)
        gekozen_speler = een_lijst[gekozen_index]
        if gekozen_speler not in selectie:
            selectie.append(gekozen_speler)
    return selectie
def opslaan_ploegopstelling(lst_namen):
    mijn_bestand = open('week6/oef04/Selectie.txt','w')
    for naam in lst_namen:
        mijn_bestand.write(naam + "\n")
    mijn_bestand.close()

spelers = inlezen_spelers('week6/oef04/Spelers.txt') #(map/bestand) als niet in zelfde map is
afprinten_spelers(spelers)
print("Geselecteerde elftal")
gekozen = selecteer_random_elftal(spelers)
afprinten_spelers(gekozen)
opslaan_ploegopstelling(gekozen)
