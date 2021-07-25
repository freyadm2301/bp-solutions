# Maak een dataklasse Winkelkar dat als private attribuut een list van producten (String) bijhoudt.
# Voorzie de klasse van volgende methodes:
# • Programmeer de methode __init__()
# • Programmeer de methode __str__()
# • ‘Read-only’ property-methode ‘producten’ dat de lijst terug geeft.
# • Methode ‘voeg_product_toe(nieuw_product)’ dat een nieuw productaan het winkelkarretje toevoegt.
# • Methode ‘verwijder_product(product)’ dat een product uit het winkelkarretje verwijdert.
# • Zorg ervoor dat de +-operator toegepast kan worden:
# o zodat twee winkelkarretjes bij elkaar kunnen opgeteld worden en een nieuw winkelkarretje opleveren
# (welke methode moet hiervoor toegevoegd worden?)
# o zodat het bestaande winkelkarretje uitgebreid wordt met de producten uit een andere winkelkarretje
# (welke methode moet hiervoor toegevoegd worden?)
# Test alles uit:
# •Maak 2 winkelkarrtjes aan.
# Voeg verschillende producten aan elk toe.
# Print nadien beide af.
# •Tel beide winkelkarrtejes op via de plus-operator.
# Print resultaat af.

class Winkelkar():
    def __init__(self):
        self.__producten = []

    # getter
    @property
    def producten(self):
        return self.__producten

    # extra functies/methode
    def voeg_toe(self, par_naam_product):
        self.__producten.append(par_naam_product)

    def verwijder(self,par_naam_product):
        self.__producten.remove(par_naam_product)

    # operator overloading self is winkelkar links van plus teken
    # other is winkelkar rechts
    # tel je in test class twee karretjes op, krijg je een nieuw
    def __add__(self, other):
        w = Winkelkar()
        w.__producten = self.__producten + other.__producten
        return w