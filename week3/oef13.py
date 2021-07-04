#Vraag aan de gebruiker een Howest studenten e-mailadres op. 
# Controleer of het opgegeven e-mail adres in een geldig formaat opgegeven is (voornaam.naam@student.howest.be)

def controlemail(email):
    if not email.endswith("student.howest.be"):
        return False
    if not "@" in email:
        return False
    positie_at = email.find("@")
    if positie_at <=0:
        return False
    return True

adres1 = "freyademuynck@howest.be"
adres2 = "freya.de.muynck@student.howest.be"
adres3 = "freya@howest.be"

if controlemail(adres1)==True:
    print("is geldig")
else:
    print("is ongeldig")