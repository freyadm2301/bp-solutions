# Schrijf een functiemet 4 parameters (a,b,c,d) die getallen voorstellen. 
# De laatste 2 parameters hebben 0 als default-waarde. 
# De functie geeft het resultaat van volgende berekening terug: a – b + c – d.
# - Roep de functie aan door 4 getallen door te geven
# - Roep de functie aan met dezelfde 4 getallen maar in andere volgorde (gebruik de parameternamen)
# - Roep de functie aan met twee getallen

def wisksom(a, b, c = 0, d = 0):
    tsom = a - b + c - d
    return tsom

print("Het resultaat van de wiskundige formule is: {0}".format(wisksom(5,3,2,1)))
print("Het resultaat van de wiskundige formule is: {0}".format(wisksom(b=3,d=1,c=2,a=5)))
print("Het resultaat van de wiskundige formule is: {0}".format(wisksom(5,3,)))