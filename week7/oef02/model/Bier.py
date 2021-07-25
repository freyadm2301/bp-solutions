# Bestudeer het bronbestand bieren.csv.
# Door welke zaken wordt een bier gekenmerkt?
# Maak nu een dataklasse Bier.
# - Voorzie de klasse van de nodige attributen en properties.
#     - In de setter wordt de nieuwe waarde  gecontroleerd: een lege string wordt naar ‘onbekend’ omgezet.
#     - Het alcoholpercentage moet tussen 0 en 100 liggen.
# - Programmeer de methode __init__()
# - Programmeer de methode __str__()

# Maak verschillende bieren aan. Wijzig nadien de attributen via de setter-methodes. Controleer of de functionaliteit in orde is.

class Bier:
    def __init__(self, par_id, par_naam, par_brouwerij, par_kleur, par_alcoholgehalte):
        self.id = par_id
        self.naam = par_naam
        self.brouwerij = par_brouwerij
        self.kleur = par_kleur
        self.alcohol = par_alcoholgehalte

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if value > 0:
            self.__id = value
        else:
            self.__id = 99999

    @property
    def naam(self):
        return self.__naam

    @naam.setter
    def naam(self, value):
        if value == '':
            self.__naam = 'ONBEKEND'
        else:
            self.__naam = value

    @property
    def brouwerij(self):
        return self.__brouwerij

    @brouwerij.setter
    def brouwerij(self, value):
        if value == "":
            self.__brouwerij = "ONBEKEND"
        else:
            self.__brouwerij = value

    @property
    def kleur(self):
        return self.__kleur

    @kleur.setter
    def kleur(self, value):
        self.__kleur = value

    @property
    def alcohol(self):
        return self.__alcohol

    @alcohol.setter
    def alcohol(self, value):
        if isinstance(value, int) or isinstance(value, float):
            if 0 < value < 100:
                self.__alcohol = value
            else:
                self.__alcohol = -1
        else:
            self.__alcohol = -1

    # methodes
    def __str__(self):
        return "{0}-{1}({2}%)".format(self.naam, self.brouwerij, self.alcohol)