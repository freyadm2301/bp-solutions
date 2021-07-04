# Vraag aan de gebruiker de basis en de hoogte van een driehoek op. 
# Bereken nadien de oppervlakte en print deze nadien af.

basis = float(input("Geef de basis van de driehoek op : "))
hoogte = float(input("Geef de hoogte van de driehoek op : "))

opp = (basis*hoogte)/2

print("De oppervlakte bedraagt {0}".format(round(opp,2)))