# Vraag een niet-decimaal getal aan de gebruiker. 
# Bepaal of het opgegeven getal even of oneven is. 
# Print een gepaste boodschap af.
getal = float(input("Geef een geheel getal op: "))

if getal%2 == 0:
    print("Het getal is even.")
else:
    print("Het getal is oneven.")