# Schrijf een functie ‘som_num_in_list’ met als parameter een list van getallen die de totale som van de list getallen teruggeeft.
lst = [9,7,13,3,11]
def som_num_in_list(list_met_getallen):
    som=0

    for getal in list_met_getallen:
        som = som + getal
    return som

print(som_num_in_list(lst))