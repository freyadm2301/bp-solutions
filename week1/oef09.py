# Vraag aan de gebruiker een int-getal n op. 
# Bereken de volgende som: n + nn + nnn. 
# Print het resultaat af.
n = int(input("Geef een getal op: "))
nn = 10*n + n
nnn = nn*10 + n
totn= n+nn+nnn
print("Het resultaat is: {0}".format(totn))