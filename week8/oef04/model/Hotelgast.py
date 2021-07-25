class Hotelgast():
    # init-> nr en gastenlist meegeven
    def __init__(self, par_naam, par_voornaam, par_adres):
        self.__naam = par_naam
        self.__voornaam = par_voornaam
        self.__adres = par_adres

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
    def adres(self):
        return self.__adres

    @adres.setter
    def adres(self, value):
        self.__adres = value

    def __str__(self):
        return "De gast: {1} - {0} : {2}".format(self.__naam,self.__voornaam,self.__adres)
    def __repr__(self):
        #als ik hotelgasten print in een list
        #dan zal str niet worden opgeroepen maar
        #zal repr worden opgeroepen
        #de repr roept op zijn beurt de str op
        return self.__str__()