#demo 1
dict_klassen ={"7BWV":16, "6WEWI":16, "6LAWEWI":2}

#optie 1
aantal = 0
#optie 2
zesde = []
for klas in dict_klassen.keys():
    eerst_letter = klas[0] #neem de 0de index
    if eerst_letter == "6":
        aantal += 1 #optie 1
        zesde.append(klas) #optiez 2
print("aantal klassen : {0}".format(aantal))
print("aantal klassen : {0}".format(zesde))
print("aantal klassen : {0}".format(len(zesde)))

def zoek_aantal_richting_met_hoofdvak(afkorting,lijst):
    aantal = 0
    for klas in lijst.keys():
        if afkorting in klas:
            aantal += 1
    return aantal
def geef_aantal_leerlingen_in_klas_met_hoofdvak(afkorting,lijst):
    aantallln = 0
    for klas, leerlingen in lijst.items():
        if afkorting.lower() in klas.lower():
            aantallln += leerlingen
    return aantallln
lln = input("Wat is het hoofdvak? (afk)")
aantal_lln = geef_aantal_leerlingen_in_klas_met_hoofdvak(lln, dict_klassen)
print("Het aantal leerlingen in {0} is: {1}".format(lln,aantal_lln))

afk = input("Welk vak wil je zoeken? (afk)")
aantal_klassen = zoek_aantal_richting_met_hoofdvak(afk,dict_klassen)
print("Aantal klassen met {0} in de naam: {1}".format(afk,aantal_klassen))

for klas in dict_klassen.keys():
    print(klas)
