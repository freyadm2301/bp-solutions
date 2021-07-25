# Maak volgende 2 dictionaries aan. Ze stellen beide de verschillende studentenaantallen per opleidingsjaar voor.
# - 'nmct' met de elementen {"1NMCT":131, "2NMCT":88, "3NMCT":77}
# - 'devine' met de elementen {"1Devine": 123, "2Devine":98, "3Devine":55}
nmct = {"1NMCT":131, "2NMCT":88, "3NMCT":77}
devine = {"1Devine": 123, "2Devine":98, "3Devine":55}

# Wat is het effect van het print-commando op een dictionary?
print(nmct)
# Hoe kan je een element uit de dictionary opvragen?
print(nmct["2NMCT"])
print(nmct.get("1NMCT","Element bestaat niet"))
print(nmct.get("1MIT","Element bestaat niet"))
# Hoe voeg je een nieuw element aan de dictionary toe?
nmct["1IPO"] = 156
print(nmct)
# Wat gebeurt er als een nieuw element met dezelfde key aan een dictionary wordt toegevoegd?
nmct["1IPO"] = 32
print(nmct)
# Hoe controleer je of een key in een dictionary reeds in gebruik is?
def key_check_nmct(key):
    if key in nmct.keys():
        print("{0}: Key is aanwezig".format(key))
    else:
        print("{0}: Key is niet aanwezig".format(key))
key_check_nmct("2NMCT")
key_check_nmct("MCT")
# Hoe kan je een key (met value) uit een dictionary verwijderen? Wat als de key niet aanwezig is?
del nmct["1IPO"]
print(nmct)
# del nmct["1IPO"] je krijgt een error