# Schrijf een functie ‘geef_gemeenschappelijke_elementen’ die 2 lists binnenkrijgt. 
# De functie bepaalt de gemeenschappelijke elementen en geeft deze als een nieuwe list terug. 
# Zorg ervoor dat er in deze laatste list geen dubbels voorkomen. 
# Print vervolgens alles af.
def geef_gemeenschappelijke_elementen(lijst1, lijst2):
    temp = []
    for item in lijst1:
        if item in lijst2:
            temp.append(item)

    res = []
    for i in temp:
        if i not in res:
            res.append(i)
    return res


getallen1 = [4,2,5,9,10,5,14]
getallen2 = [2,5,10,11,3,2]

unieg = geef_gemeenschappelijke_elementen(getallen1,getallen2)
print(unieg)