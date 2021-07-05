# Schrijf een functie ‘kies_5_getallen’ die twee waarden (min en max) als parameter binnenkrijgt. 
# De functie kiest 5 unieke getallen uit het interval [min,max], voegt deze toe aan een list en geeft uiteindelijk deze list terug. 
# opgelet: er mogen geen dubbels in de teruggegeven lijst voorkomen. 
# Test voldoende uit.
import random

def kies_5_getallen(min, max):
    temp = []
    while len(temp) < 5:
        getal = random.randint(min,max)
        if not getal in temp:
            temp.append(getal)
    return temp

print(kies_5_getallen(10,30))