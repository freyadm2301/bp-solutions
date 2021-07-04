# Maak een functie met als parameters minimum_lengte en maximum_lengte. De functie genereert een willekeurig paswoord bestaande uit een combinatie van kleine en hoofdletters, én  waarvan de lengte van het genereerde paswoord tussen beide grenzen valt.

import random
import string
def genereerpas(min,max):
    aantaltekens = random.randint(min,max)
    paswoord = ""
    for teller in range(0,aantaltekens):
        paswoord += random.choice(string.ascii_letters)

    return paswoord
print(genereerpas(5,9))