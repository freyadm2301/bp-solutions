# Maak een lege list ‘vrienden’ aan. 
# We laten de applicatie deze list dynamisch uitbreiden. 
# Telkens wordt aan de gebruiker gevraagd om een nieuwe naam op te geven of een lege string. 
# In dat laatste geval stopt de applicatie door de lijst met vrienden af te printen.

list = []
vriend = input("Geef de naam van een vriend op, of sluit af met een leeg veld: ")

while vriend != "":
    list.append(vriend)
    vriend = input(" Geef de naam van een vriend op, of sluit af met een leeg veld: ")
print('Uw vrienden zijn:',list)