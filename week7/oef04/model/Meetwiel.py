# We wensen van elk wiel de straal en het aantal omwentelingen bijhouden.
# Hiervoor maken we een klasse Meetwiel met de instantie-attributen ‘straal’en‘omwentelingen’(default-waarde:0).
# Volgend stappenplan kan gevolgd worden:
# Voorzie de klasse van de nodige attributen en bijhorende properties.
# Voorzie 2 extra property-methodes:
# Programmeer de property-methode omtrek():deze geeft de omtrek van het wiel terug
# Programmeer de property-methode afstand(): deze geeft de afgelegde afstand ifv de het aantal omwentelingen en de omtrek van het meetwiel terug.
# Programmeer de methode __init__()
# Programmeer de methode __str__()
# Test voldoende uit door verschillende objecten van deze klasse aan te maken.
# Vraag tenslotte aan de gebruiker meerdere extra omwentelingen voor een wiel op.
# Sluit af met ‘c’. Print nadien de afgelegde afstand opnieuw af.
import math

class Meetwiel():
    def __init__(self, par_straal, par_omwentelingen):
        self.__straal = par_straal
        self.omwentelingen = par_omwentelingen

    @property
    def straal(self):
        return self.__straal

    @property
    def omwentelingen(self):
        return self.__omwentelingen

    @omwentelingen.setter
    def omwentelingen(self, value):
        if value > 0 :
            self.__omwentelingen = value
        else:
            self.__omwentelingen = 0

    @property
    def afstand(self):
        return self.omwentelingen * self.omtrek

    @property
    def omtrek(self):
        return 2 * self.straal * math.pi

    def __str__(self):
        return 'Meetwiel met straal {0} en omwentelingen {1}'.format(self.__straal, self.omwentelingen)

    def doe_extra_omwentelingen(self, par_aantal):
        par_aantal = input('Geef het aantal omwenteling of sluit af met c: ')
        while par_aantal != 'c' or 'C':
            if isinstance(par_aantal,int):
                self.omwentelingen += par_aantal

            elif par_aantal == 'c':
                return self.omwentelingen and print('Het meetwiel legde reeds {0} meter af '.format(self.afstand))
            par_aantal = input('Geef het aantal omwenteling of sluit af met c: ')
