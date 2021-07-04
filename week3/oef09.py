# Laat je applicatie een getal kiezen tussen 1 en 20. 
# Laat vervolgens de gebruiker naar het getal raden. 
# Bij iedere poging krijgt hij feedback: “kleiner” of “groter”.
# De applicatie stopt pas als het getal geraden is
import random

invoer_gebruiker = 0
te_raden_getal = random.randint(1,20)

invoer_gebruiker = int(input("Raad het getal "))

while invoer_gebruiker != te_raden_getal:
    if invoer_gebruiker < te_raden_getal:
        print("Het getal was te klein")
    else:
        print("Het getal was te groot")

    invoer_gebruiker = int(input("Raad het getal "))
print("Je hebt het geraden")
print("Stop")