# Maak een functie 'geef_dict' die een dictionary teruggeeft waarbij de keys lopen van 1 tem 20 en de values steeds het kwadraat van de key zijn.
def geef_dict():
    kwadraten = dict()
    for i in range (1, 21):
        kwadraten[i] = i**2
    return kwadraten

print(geef_dict()) 