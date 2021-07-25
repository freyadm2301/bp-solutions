# Gegeven het bronbestand ‘Scores.txt’.
# Analyseer het bronbestand: elke lijn bestaat uit de gegevens van een student gevolgd door 5 scores.
# Maak nu een applicatie die na het inlezen van het bronbestand op basis van de naam de scores van een student(en) kan opzoeken,
# en onmiddellijk ook de gemiddelde score van elke student afprint.
# Bepaal vooraf welke datastructuur je zal gebruiken om alle data bij te houden.
# Werk vervolgens in deelproblemen:
# - Een functie ‘inlezen_scores_studenten’ staat in voor het inlezen van het bronbestand
# - Een functie ‘zoek_student’ zoekt de scores van een student op en print deze af.

dict_studenten = {}

def inlezen_scoren_studenten(path):
    dict_temp = {}
    fo = open(path, 'r')
    lijn = fo.readline().rstrip('\n')
    while lijn != '':
        #afzonderen naam en punten
        lijn_naar_lijst = lijn.split(':')
        naam = lijn_naar_lijst[0]
        punten = lijn_naar_lijst[1:]
        #temp dict opbouwen
        dict_temp[naam] = punten

        lijn = fo.readline().rstrip('\n')
    fo.close()
    return dict_temp

def maak_gem(naam, dict_te_zoeken):
    lst_punten = dict_te_zoeken[naam]
    som = 0
    for punt in lst_punten:
        som += int(punt) #waren strings

    return som/len(lst_punten)

dict_studenten = inlezen_scoren_studenten('week6/oef05/Scores.txt')
print(dict_studenten)
naam = input('Van wie wil je de resultaten zien? ')
gem = maak_gem(naam, dict_studenten)
print('behaalde {0}'.format(gem))