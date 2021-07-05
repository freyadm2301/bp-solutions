# Maak volgende lists aan:
# - een list met 4 gehele getallen
# - een list met 5 decimale getallen
# - een list met 3 strings
# Maak nu één functie ‘print_list’ die de verschillende elementen overloopt waarbij elk element samen met zijn index wordt afgeprint.

lijst1 = [12,45,-9,-15]
lijst2 = [12.23,45.1,9.478,15.125,-3.14]
lijst3 = ["Stijn","Lies","Henk"]



def print_lijst(omschrijving,een_lijst):
    print("Verzameling {0}:".format(omschrijving))
    for element in een_lijst:
        print('{0} zit op positie {1}'.format(element, een_lijst.index(element)))

print_lijst("gehele getallen",lijst1)
print_lijst("decimale getallen",lijst2)
print_lijst("strings",lijst3)