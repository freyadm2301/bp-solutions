# Maak een klasse Speler die naast een naam en voornaam ook een individuele score bijhoudt.
# Voorzie de klasse nu van:
# - de gevraagde properties met de nodige inputvalidatie
# - de klassieke methodes __init__() en __str__()

# Breid nu deze klasse uit zodat ook de totale score van het volledige team kan opgevraagd worden:
# dit is de som van alle individuele scores.
# (Let op: deze teamscore is voor elke speler gelijk)
# Voorzie een static-methode om deze teamscore terug te geven.
# Test uit door verschillende objecten van deze klasse aan te maken.

from week8.oef02.model.Geboortedatum import Geboortedatum


class Speler():
    __score_team = 0

    def __init__(self, par_naam, par_voornaam, par_score_speler, par_geboortedatum = Geboortedatum(1, 1, 2017)):
        # rechtstreeks de private attributen instellen (als er geen SETTER zou zijn)
        # self.__naam = par_naam
        # self.__score_speler = par_score_speler
        # Speler.__score_team += par_score_speler
        # self.__voornaam = par_voornaam

        #   of via de properties (aanpassing teamscore gebeurt in de setter van de score_speler)
        self.naam = par_naam
        self.voornaam = par_voornaam
        self.score = par_score_speler
        self.geboortedatum = par_geboortedatum
        Speler.__score_team += par_score_speler

    @property
    def naam(self):
        return self.__naam

    @naam.setter
    def naam(self, value):
        self.__naam = value

    @property
    def voornaam(self):
        return self.__voornaam

    @voornaam.setter
    def voornaam(self, value):
        self.__voornaam = value

    @property
    def score(self):
        return self.__score_speler

    @score.setter
    def score(self, value):
        if isinstance(value, int):
            # indien men in de init-methode van de property score_speler gebruik maakt
            # moet men eerst controleren of er al een oude waarde aanwezig is...
            if hasattr(self, '__score_speler'):
                # teamscore eerst verminderen met zijn oude waarde
                Speler.__score_team -= self.score
            self.__score_speler = value
            # teamscore aanpassen
            Speler.__score_team += value
        else:
            self.__score_speler = 0

    def __str__(self):
        return 'Speler {0} {1} heeft een score van {2}'.format(self.voornaam, self.naam, self.score)

    @staticmethod
    def score_team():
        return Speler.__score_team