# Vraag aan de gebruiker twee int-getallen n op. 
# Bereken nu volgend resultaat: (x + y) * (x + y). 
# Print het resultaat af.

x = int(input("Geef een getal op: "))
y = int(input("Geef een getal op: "))
totxy = (x + y)*(x + y)
print("(({0} + {1}) ^ 2) = {2}".format(x,y,totxy))