# We integreren vorige oefeningen in elkaar. Zorg ervoor dat van elke speler ook de geboortedatum
# (object van de klasse Geboortedatum) wordt bijgehouden.
# Print van elke aangemaakte speler nu ook zijn geboortedatum af.

from week8.oef02.model.Geboortedatum import Geboortedatum
from week8.oef01.model.Speler import Speler


def test_spelers_oef3():
    sp1 = Speler("Stijn", "Walcarius", 10, Geboortedatum(25,9,1977))
    sp2 = Speler("Lode", "Vlaeminck", 20)

    list_spelers = [sp1, sp2]

    for speler in list_spelers:
        print("{0} -> gebootedatum: {1}".format(speler,speler.geboortedatum))

test_spelers_oef3()