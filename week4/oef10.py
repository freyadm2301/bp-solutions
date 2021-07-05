# Schrijf een functie ‘zijn_verschillend’ die 2 lists binnenkrijgt. 
# De functie geeft False terug indien er minimum één gemeenschappelijk element gevonden wordt.
# True wordt pas terug gegeven als beide helemaal verschillend zijn.
def zijn_verschillend(lijst1, lijst2):
    uitkomst = False
    for naam in lijst1:
        if not naam in lijst2:
            uitkomst = True
        else:
            return False
    return uitkomst

klas = ["jan", "piet", "linda"]
vrienden = ["jan","linda","rick"]

if zijn_verschillend(klas,vrienden) == True:
    print("beide lijsten zijn verschillend")
else:
    print("Er zit min 1 gemeenschappelijk element in de lijsten")