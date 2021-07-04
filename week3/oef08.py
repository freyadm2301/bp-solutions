# Print de som van de eerste 100 getallen. Gebruik hiervoor een while-lus.
som = 0
teller = 1

while teller <= 100:
    som = som + teller
    teller += 1
    print("subtotaal = {0}".format(som))
print("Totaal = {0}".format(som))
print("Stop")