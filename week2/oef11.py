# Schrijf een functie die 3 getallen binnenkrijgt. 
# De functie geeft het maximum terug.
def Max(X,Y,Z):
    if X >= Y:
        Temp_grootst = X
    else:
        Temp_grootst = Y
    if Temp_grootst >= Z:
        Temp_grootst = Temp_grootst
    else:
        Temp_grootst = Z

    return Temp_grootst

x = int(input("Geef getal 1: "))
y = int(input("Geef getal 2: "))
z = int(input("Geef getal 3: "))

max = Max(x,y,z)
print("Het grootste getal is {0}".format(max))