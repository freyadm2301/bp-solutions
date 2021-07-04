# Vraag aan de gebruiker zijn naam, voornaam en geboortedatum (formaat: dd-mm-yyyy) op. 
# Genereer hiermee een paswoord door:
# - de eerste 3 karakters van de ingegeven familienaam (in kleine letters en zonder de eventuele spaties mee te nemen)
# - de eerste 2 karakters van de voornaam (in hoofdletters en ook zonder spaties)
# - 4 cijfers (mmyy) uit de geboortedatum.
# Maak hiervoor een afzonderlijke functie ‘genereer_paswoord’

def genereerpaswoord(naam,voornaam,geb):
    naam = naam.replace(" ","")
    deel_naam = naam[0:3]
    deel_voornaam = voornaam[0:2]
    deel_geb = geb[3:5]+geb[-2:]
    return deel_naam.lower()+deel_voornaam.upper()+deel_geb
print(genereerpaswoord("De Muynck ", "Freya", "23-01-2001"))
n= input("Geef uw naam op: ")
v= input("Geef uw voornaam op: ")
g = input("Geef uw geboortedatum op (dd-mm-yyyy): ")
print(genereerpaswoord(n,v,g))