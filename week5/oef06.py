def print_dictionary(naam, dictionary):
    print('Dictionary {0}:'.format(naam))
    for klas in dictionary.keys():
        print("key: {0} -> value: {1}".format(klas, dictionary[klas]))

Howest = {"1NMCT":131, "2NMCT":88, "3NMCT":77, "1Devine": 123, "2Devine":98, "3Devine":55}

# Maak een methode 'voeg_nieuw_element_toe' aan die een nieuw element aan de dictionary toevoegd nadat er eerst gecontroleerd wordt of de key nog niet in gebruik is. Indien de key al in gebruik is, wordt er een foutboodschap afgeprint.
# De methode heeft als parameters de key, de value en de dictionary zelf.

# Test dit uit door aan dictionary Howest achtereenvolgens toe te voegen
# - element met key '1IPO' met de waarde '51'
# - element met key '1IPO' met de waarde '10'

# print nadien telkens de dictionary Howest af (via methode uit oefening 4).
def voeg_nieuw_element_toe(given_key, given_value, given_dict):
    if given_key in given_dict.keys():
        print("Toevoegen mislukt. Key '{0}' reeds aanwezig".format(given_key))
    else:
        given_dict[given_key] = given_value
        print_dictionary('Howest', given_dict) 

voeg_nieuw_element_toe('1IPO',51,Howest)
voeg_nieuw_element_toe('1IPO',10,Howest)
