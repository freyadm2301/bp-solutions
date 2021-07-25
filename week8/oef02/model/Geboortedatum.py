# Maak een dataklasse Geboortedatum.
# Zorg ervoor dat dag, maand en jaartal bijgehouden worden.
# Voorzie nu zelf de klasse van:
# - De gevraagde properties.
# Bouw controles in wanneer dag/maand/jaartal gewijzigd worden.
# - Programmeer de methode __init__()
# - Programmeer de methode __str__()

# Breid de klasse nu vervolgens uit:
# - Hou het aantal gecreërde objecten van de klasse Geboortedatum bij.
# - Maak een static methode om deze property op te vragen.
# - Maak een static methode die een willekeurige geboortedatum genereert.
# - Maak een static methode die een list van willekeurige geboortedatums genereert en terug geeft
# - De parameter is het gewenste aantal.
# - Integreer een methode die instaat om de gelijkheid tussen twee geboortedatums te controleren.
# Bepaal eerst vooraf wanneer twee geboortedatums aan elkaar gelijk zijn.
# (Tip: gebruik operator overloading!)
# - Maak een (gewone) methode met als parameter een object Geboortedatum,
# die controleert of beide op dezelfde dag verjaren (m.a.w. dag & maand zijn gelijk)

# Test uit door verschillende objecten van deze klasse aan te maken.
# Plaats deze test in een ander afzonderlijk python-bestand.

from datetime import datetime
import random

class Geboortedatum:
    __aantal_data = 0  #private static attribuut
    
    def __init__(self, par_dag, par_maand, par_jaar):
        # volgorde belangrijk: eerst maand, dan dag -> controle waarde dag op basis van maand
        self.jaar = par_jaar
        self.maand = par_maand
        self.dag = par_dag
        Geboortedatum.__aantal_data += 1
    
    @property
    def jaar(self):
        return self.__jaar
    
    @jaar.setter
    def jaar(self, value):
        if isinstance(value, int):
            self.__jaar = value
        else:
            self.__jaar = -1
            
    @property
    def maand(self):
        return self.__maand
    
    @maand.setter
    def maand(self, value):
        if isinstance(value,int) and value in range(1,13):
            self.__maand = value
        else:
            self.__maand = -1

    @property
    def dag(self):
        return self.__dag

    @dag.setter
    def dag(self, value):
        if isinstance(value, int) and self.controleer_dag(value):
            self.__dag = value
        else:
            self.__dag = -1

    def __str__(self):
        return str(self.__dag) + '/' + str(self.__maand) + '/' + str(self.__jaar)

    #gelijkheid
    def __eq__(self, other):
        if (self.jaar == other.jaar) and (self.maand == other.maand) and (self.dag == other.dag):
            return True
        else:
            return False

    def controleer_dag(self, nieuwe_dag):
        if self.__maand in [1, 3, 5, 7, 8, 10, 12]:
            if nieuwe_dag in range(1, 32):
                return True
        elif self.__maand in [4, 6, 9, 11]:
            if nieuwe_dag in range(1, 31):
                return True
        else:
            if nieuwe_dag in range(1, 30):
                return True
        return False

    @staticmethod
    def geef_aantal_geboortedatums():
        return Geboortedatum.__aantal_data
