# Vraag aan de gebruiker het aantal dagen, uren, minuten en seconden op. 
# Bepaal het totale aantal seconden.

dagen = int(input("Geef het aantal dagen op: "))
uren = int(input("Geef het aantal uren op: "))
minuten = int(input("Geef het aantal minuten op: "))
seconden = int(input("Geef het aantal seconden op: "))

dsec = dagen*24*60*60
usec = uren*60*60
msec = minuten*60
sec = dsec + usec + msec + seconden

print("Het totale aantal seconden bedraagt: {0}".format(sec))