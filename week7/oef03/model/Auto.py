# Maak een dataklasse Auto waarbij volgende zaken worden bijgehouden:
# kleur, merk, brandstof, model, km-stand.
# Hoe kan je er voor zorgen dat enkel de attributen km-stand en kleur nadien gewijzigd kunnen worden?
# Voeg ook een methode ‘rijden’ met de parameter extra_km toe:
# hiermee wordt de km-stand van de auto verhoogd.
# Test alles uit: maak een list aan met verschillende voertuigen. 
# Laat vervolgens elk voertuig uit de list een random afstand afleggen. 
# Print nadien van elk voertuig de km-stand af.

class Auto:
    def __init__(self, par_kleur, par_merk, par_brandstof, par_model, par_kmstand):
        self.kleur = par_kleur
        self.__merk = par_merk
        self.__brandstof = par_brandstof
        self.__model = par_model
        self.kmstand = par_kmstand

    @property
    def merk(self):
        return self.__merk

    @property
    def model(self):
        return self.__model

    @property
    def brandstof(self):
        return self.__brandstof

    @property
    def kleur(self):
        return self.__kleur

    @kleur.setter
    def kleur(self, value):
        self.__kleur = value

    @property
    def kmstand(self):
        return self.__kmstand

    @kmstand.setter
    def kmstand(self, value):
        if value >= 0:
            self.__kmstand = value
        else:
            self.__kmstand = 'ONGELDIG'

    def __str__(self):
        return '{0} (model: {1} kleur: {2}) '.format(self.__merk, self.__model, self.kleur)

    def rijden(self, par_km):
        self.kmstand += par_km