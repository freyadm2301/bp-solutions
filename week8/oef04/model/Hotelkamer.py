class Hotelkamer:
    # init -> nr (A1) en gastenlist meegeven
    # list is private geen setter
    # default is de list leeg als parameter
    def __init__(self, nr, list_met_gasten=[]):
        self.nr = nr
        self.__gastenlijst = list_met_gasten

    @property
    def nr(self):
        return self.__nr

    @nr.setter
    def nr(self, value):
        self.__nr = value

    @property
    def gastenlijst(self):
        return self.__gastenlijst

    def voeg_gast_toe(self, nieuwe_gast):
        self.gastenlijst.append(nieuwe_gast)

    def is_beschikbaar(self):
        if len(self.gastenlijst) == 0:
            return True
        else:
            return False

    def check_out(self):
        self.__gastenlijst = []

    def __str__(self):
        return "Kamer {0} met gasten {1}".format(self.nr, self.__gastenlijst)


