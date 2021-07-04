# Schrijf een functie ‘swap’ die twee strings binnenkrijgt. 
# De functie stelt één nieuwe string op waarbij de twee letters van elk woord worden omgewisseld 
# en beide nieuwe woorden door een spatie gescheiden worden.

woord1 = "abc"
woord2 = "xyz"

beginwoord1 = woord1[0:2]
eindwoord1 = woord1[2]
beginwoord2 = woord2[0:2]
eindwoord2 = woord2[2]

resultaat = beginwoord1 + eindwoord2 + "->"+ beginwoord2 + eindwoord1
print(resultaat)