# Vraag aan de gebruiker een aantal seconden op. 
# Zet dit aantal om in dagen, uren, minuten en seconden.

totaal_sec = int(input("Geef het aantal seconden op: "))

d = totaal_sec//(24*3600)
overschot_sec = totaal_sec%(24*3600)
h = overschot_sec//(3600)
overschot_sec = overschot_sec%(3600)
m = overschot_sec//(60)
overschot_sec = overschot_sec%60
s = overschot_sec

print("d:h:m:s-> {0}:{1}:{2}:{3}".format(d,h,m,s))