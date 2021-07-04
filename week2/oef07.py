# Vraag aan de gebruiker twee woorden op. 
# Ga na of deze aan elkaar gelijk zijn (zonder rekening te houden met kleineletters of hoofdletters)
woord1 = input("Geef een woord: ")
woord2 = input("Geef een woord: ")

if woord1.lower() == woord2.lower():
    print("De woorden zijn gelijk")
else:
    print("De woorden zijn niet gelijk.")