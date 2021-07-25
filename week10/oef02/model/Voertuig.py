import uuid

class Voertuig():
    __aantal_voertuigen = 0

    def __init__(self, par_merk, par_bouwjaar, par_aantalkm, par_reisbestemming = ''):
        self.merk = par_merk
        self.bouwjaar = par_bouwjaar
        self.aantalkm = par_aantalkm
        self.reisbestemming = par_reisbestemming
        self.__id = uuid.uuid4()
        Voertuig.__aantal_voertuigen += 1

    @property
    def id(self):
        return self.__id

    @property
    def merk(self):
        return self.__merk

    @merk.setter
    def merk(self, value):
        self.__merk = value

    @property
    def bouwjaar(self):
        return self.__bouwjaar

    @bouwjaar.setter
    def bouwjaar(self, value):
        if isinstance(value, int):
            self.__bouwjaar = value
        else:
            self.__bouwjaar= 'Fout'

    @property
    def aantalkm(self):
        return self.__aantalkm

    @aantalkm.setter
    def aantalkm(self, value):
        if isinstance(value, float):
            self.__aantalkm = value
        else:
            self.__aantalkm = 'Fout'

    @property
    def reisbestemming(self):
        return self.__reisbestemming

    @reisbestemming.setter
    def reisbestemming(self, value):
        self.__reisbestemming = value

    def __str__(self):
        return "Voertuig {0} {1} ".format(self.merk, self.bouwjaar)

    def geef_detail_info(self):
        return "geen info beschikbaar."

    @staticmethod
    def geef_aantal_voertuigen():
        return Voertuig.__aantal_voertuigen