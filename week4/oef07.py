# Schrijf een functie ‘max_num_in_list’ met als parameter een list van getallen die uit de list het maximum opzoekt en teruggeeft.
def max_num_in_list(list_met_getallen):
    list_met_getallen.sort()
    list_met_getallen.reverse()
    return list_met_getallen[0]
lst = [9,7,13,3,11]
print(max_num_in_list(lst))