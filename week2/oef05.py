# Vraag de decimale score van een module aan de gebruiker. 
# Print nadien af of hij/zij geslaagd is. 
# Zorg ervoor dat de score correct afgerond wordt: indien het decimale gedeelte kleiner is dan 0,5 wordt er naar beneden afgerond. 
# In het andere geval wordt er naar boven afgerond. Print ook de afgeronde score af.

komma_getal = float(input("Geef uw score op: "))
geheel_deel = komma_getal//1
decimaal_deel = komma_getal%1

if komma_getal >= 9.5:
    print("U bent geslaagd.")
else:
    print("Helaas volgende keer beter")
if decimaal_deel < 0.5:
    print("Wetenschappelijk afgerond wordt dat {0}".format(geheel_deel))
else:
    print("Wetenschappelijk afgerond wordt dat {0}".format(geheel_deel+1))