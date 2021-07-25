nmct = {"1NMCT":131, "2NMCT":88, "3NMCT":77}
devine = {"1Devine": 123, "2Devine":98, "3Devine":55}
# Maak nu één functie 'print-dictionary' die de verschillende elementen overloopt waarbij telkens key & value samen op één lijn worden afgeprint.
# De functie heeft als parameters een naam (voor de dictionary) en de dictionary zelf.

def print_dictionary(naam, dictionary):
    print('Dictionary {0}:'.format(naam))
    for klas in dictionary.keys():
        print("key: {0} -> value: {1}".format(klas, dictionary[klas]))
    
print_dictionary("NMCT", nmct)
print_dictionary("Devine", devine)
