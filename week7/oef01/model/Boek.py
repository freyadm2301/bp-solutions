# Maak een dataklasse Boek.
# Wat zijn de kenmerken waarmee een boek zich kan identificeren?
# Codeer nu deze dataklasse:
# - Voorzie de klasse van de nodige attributen en properties.
# - Programmeer de methode __init__()
# - Programmeer de methode __str__()

# Test uit door verschillende objecten van deze klasse aan te maken.
# Gebruik hiervoor een afzonderlijk bestand.

class Boek:
    def __init__(self, par_titel, par_auteur, par_aantal_blz):
        self.titel = par_titel
        self.auteur= par_auteur
        self.aantal_blz = par_aantal_blz

    #properties
    @property
    def titel(self):
        return self.__titel

    @titel.setter
    def titel(self, value):
        self.__titel = value

    @property
    def auteur(self):
        return self.__auteur

    @auteur.setter
    def auteur(self, value):
        self.__auteur = value
    
    @property
    def aantal_blz(self):
        return self.__aantal_blz

    @aantal_blz.setter
    def aantal_blz(self, value):
        if isinstance(value, int):
            self.__aantal_blz = value
        else:
            self.__aantal_blz = "ONBEKEND"

    #methodes
    def __str__(self):
        return 'BOEK: {0}, {1} ({2} blz) '.format(self.titel, self.auteur, self.aantal_blz)
