from model.Winkelkar import Winkelkar

ikea_kar = Winkelkar()
fnac_kar = Winkelkar()

ikea_kar.voeg_toe('Eket')
ikea_kar.voeg_toe('Malm')
fnac_kar.voeg_toe('Iphone 6')
fnac_kar.verwijder('Iphone 6')
fnac_kar.voeg_toe('Filmbox')
print(ikea_kar.producten)
print(fnac_kar.producten)

totaal_kar = fnac_kar + ikea_kar
print(totaal_kar.producten)