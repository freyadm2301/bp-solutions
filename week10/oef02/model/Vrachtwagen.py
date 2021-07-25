from model.Voertuig import Voertuig


class Vrachtwagen(Voertuig):
    def __init__(self, par_merk, par_bouwjaar, par_aantalkm, par_max_laad_vermogen):
        #super().__init__(par_merk, par_bouwjaar, par_aantalkm)
        Voertuig.__init__(self, par_merk, par_bouwjaar, par_aantalkm)
        self.max_laad_vermogen = par_max_laad_vermogen
        self.vracht = 0


    @property
    def max_laad_vermogen(self):
        return self.__max_laad_vermogen

    @max_laad_vermogen.setter
    def max_laad_vermogen(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__max_laad_vermogen = value
        else:
            self.__max_laad_vermogen = 'Fout'

    @property
    def vracht(self):
        return self.__vracht

    @vracht.setter
    def vracht(self, value):
        if isinstance(value, int) or isinstance(value, float):
            if value <= self.__max_laad_vermogen:
                self.__vracht = value
            else:
                self.__vracht = 'FOUT: TE ZWAAR'
        else:
            self.__vracht = 'FOUT: NIET GELDIG'

    def __str__(self):
        return 'Vrachtwagen ' + Voertuig.__str__(self)

    def geef_detail_info(self):
        info = 'Detail info over vrachtwagen {0} {1}:\n'.format(self.merk, self.bouwjaar)
        info += "- ID: {0}\n".format(self.id)
        info += '- Reisbestemming: '
        if self.reisbestemming == '':
            info += 'Onbekend\n'
        else:
            info += self.reisbestemming + '\n'
        info += '- Max laadvermogen: {0}\n'.format(self.max_laad_vermogen)
        info += '- Gewicht vracht: {0}'.format(self.__vracht)
        return info