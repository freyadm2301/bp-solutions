# Schrijf een functie ‘tel_elementen_binnen_interval’ met drie parameters: een list, een minimum en een maximum. 
# De functie telt hoeveel elementen uit de list binnen het interval [min, max] vallen en geeft dat aantal terug.
def tel_elementen_binnen_interval(lst, min, max):
    temp = []
    for item in lst:
        if item >= min and item <= max:
            temp.append(item)
    return len(temp)

getallen = [6,2,10,9,8,1,11]
print(tel_elementen_binnen_interval(getallen,5,10))