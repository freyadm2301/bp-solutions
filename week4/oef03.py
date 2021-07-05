# Maak een lege list ‘nieuwe_list_getalllen’ aan. 
# Vul deze list op met getallen startend vanaf 1, met stapgrootte 13, tem 482. 
# Vervolgens:
# - Print de list af.
# - Print de list in omgekeerde volgorde af.
# - Verwijder het eerste element en print opnieuw de list af.
# - Zoek de werkwijze om een specifiek element uit de list te verwijderen.
# - Hoe kan je op eenvoudige wijze het laatste element uit de list afprinten?
list_nieuwe_getallen = []
for getal in range(1,483,13):
    list_nieuwe_getallen.append(getal)
print(list_nieuwe_getallen)
print("***********************************************************************************************************")
list_nieuwe_getallen.reverse()
print(list_nieuwe_getallen)
print("***********************************************************************************************************")
list_nieuwe_getallen2 = []
for getal in range(1,483,13):
    list_nieuwe_getallen2.append(getal)
del list_nieuwe_getallen2[0]
print(list_nieuwe_getallen2)
print("***********************************************************************************************************")
del list_nieuwe_getallen2[3]
print(list_nieuwe_getallen2)
print("***********************************************************************************************************")
del list_nieuwe_getallen2[-1]
print(list_nieuwe_getallen2)