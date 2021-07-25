# Maak een functie ‘tel_voorkomen_woorden’ met als parameter een string. 
# De functie geeft een dictionary terug waarbij de keys de verschillende woorden uit de zin zijn en de bijhorende values het aantal keer is dat het woord in de zin voorkomt.
# Print nadien de dictionary af.
def print_dictionary(naam, dictionary):
    print('Dictionary {0}:'.format(naam))
    for klas in dictionary.keys():
        print("key: {0} -> value: {1}".format(klas, dictionary[klas]))

def  tel_voorkomen_woorden(zin):
    resultaat = {}
    list_met_woorden = zin.split(" ")
    #overloop een list
    for woord in list_met_woorden:
        woord = woord.lower()
        if woord in resultaat.keys():
            resultaat[woord]= resultaat[woord]+ 1
        else:
            resultaat[woord]= 1
    return resultaat

mijn_zin = "Dit is nmct is het niet waar ? NMCT"
print_dictionary('Woorden_dict',tel_voorkomen_woorden(mijn_zin))