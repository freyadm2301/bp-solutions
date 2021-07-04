# Print de som van de eerste 100 getallen. Gebruik een for-lus.

som = 0
for getal in range(1,101):
    som = som + getal

print("Totale som : {0}".format(som))