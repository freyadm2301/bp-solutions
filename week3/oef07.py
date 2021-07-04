# Vraag aan de gebruiker volgende 3 getallen op:
# - een startwaarde
# - een positieve stapgrootte
# - het gewenste aantal af te printen getallen
# Schrijf een functie ‘print_lijst_getallen’ dat deze 3 getallen als parameter binnen krijgt. 
# De functie print een lijst, met het gewenste aantal getallen, 
# af waarbij het eerste getal gelijk is aan de startwaarde en de getallen met de stapgrootte vergroten.
start = int(input("Geef een startwaarde op: "))
stap = int(input("Geef een positieve stapgroote op: "))
aantal = int(input("Hoeveel getallen moeten er afgeprint worden? "))
getallen = []
def print_lijst_getallen(start, aantal, stap=1):
    for getal in range(start, (aantal-1)*stap+start+1,stap):
        getallen.append(getal)
    print(getallen)

print_lijst_getallen(start,aantal, stap)