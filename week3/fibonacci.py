# Schrijf een programma dat de rij van Fibonacci afprint voor een gegeven aantal termen.
n = int(input("aantal termen"))
add1 = 1
add2 =0
i = 1
som = 0
while i <= n:
    print(som, end='\t')
    som += add1
    add1 = som +add1
    add2 = add1 +add2
    i +=1

