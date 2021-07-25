from model.Persoon import Persoon
class Docent(Persoon):
    def __init__(self,par_naam, par_voornaam, par_pers_nr, par_opleiding, par_geboortedatum = 1980):
        Persoon.__init__(self, par_naam, par_voornaam, par_geboortedatum)
        # Hier schrijf ik rechtstreeks weg op geheugen
        self.__personeelsnummer = par_pers_nr
        self.__opleidingen = par_opleiding
