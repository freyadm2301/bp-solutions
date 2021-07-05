# Schrijf een functie ‘verwijder_duplicaten’ die een list als parameter heeft. 
# Deze functie geeft een nieuwe list zonder duplicaten terug.
# Test uit door de beide lists af te printen.
def verwijder_duplicaten(lijst):
    uitkomst = []
    for i in lijst:
        if i not in uitkomst:
            uitkomst.append(i)
    return uitkomst

getallen = [4,2,5,9,10,2,14,4,9]

uniev = verwijder_duplicaten(getallen)
print(uniev)