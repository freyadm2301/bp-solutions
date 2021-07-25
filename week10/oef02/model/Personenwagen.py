from model.Voertuig import Voertuig


class Personenwagen(Voertuig):
    def __init__(self, par_merk, par_bouwjaar, par_aantalkm, par_max_aantal_zitplaatsen):
        Voertuig.__init__(self, par_merk, par_bouwjaar, par_aantalkm)
        self.max_aantal_zitplaatsen = par_max_aantal_zitplaatsen
        self.aantal_personen = 0


    @property
    def max_aantal_zitplaatsen(self):
        return self.__max_aantal_zitplaatsen

    @max_aantal_zitplaatsen.setter
    def max_aantal_zitplaatsen(self, value):
        if isinstance(value, int):
            if value > 0 :
                self.__max_aantal_zitplaatsen = value
            else:
                self.__max_aantal_zitplaatsen = 'ERROR'
        else:
            self.__max_aantal_zitplaatsen = 'ERROR'

        @property
        def aantal_personen(self):
            return self.__aantal_personen

        @aantal_personen.setter
        def aantal_personen(self, value):
            if isinstance(value, int):
                if value >= 0:
                    self.__aantal_personen = value

    def __str__(self):
        return 'Personenwagen ' + Voertuig.__str__(self)

    def geef_detail_info(self):
        info = 'Geef detail over personenwagen {0} {1}\n'.format(self.merk, self.bouwjaar)
        info += '- ID: {0}\n'.format(self.id)
        info += '- Reisbestemming: '
        if self.reisbestemming == '':
            info += 'Onbekend\n'
        else:
            info += self.reisbestemming + '\n'
        info += '- Aantal zitplaatsen: {0}\n'.format(self.max_aantal_zitplaatsen)
        info += '- Aantal vrrije plaatsen: {0}\n'.format(self.max_aantal_zitplaatsen - self.aantal_personen)
        return info
