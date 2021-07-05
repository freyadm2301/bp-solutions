# Schrijf een functie ‘gemiddelde_in_list’ met als parameter een list van getallen die het gemiddelde van de getallen teruggeeft.
list_get = [9,7,15,84,65,98,74,62]
lst = [9,7,3,11]

def gemiddelde_in_list(list_met_getallen):
    som = 0
    for getal in list_met_getallen:
        som = som + getal
    gem = som / len(list_met_getallen)
    return gem
    
print(gemiddelde_in_list(list_get))
print(gemiddelde_in_list(lst))
