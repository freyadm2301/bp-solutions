# Schrijf volgende twee functies:
# - Eerste functie:‘geef_celsius’ krijgt een temperatuur in Fahrenheit binnen. 
#   De overeenkomstige temperatuur in Celsius wordt berekend en teruggegeven.
#   De formule is: temp = (t_in_fahrenheit - 32) * 5 / 9
# - Tweede functie:‘geef_fahrenheit’ krijgt een temperatuur in Celsius binnen. 
#   De overeenkomstige temperatuur in Fahrenheit wordt berekend en teruggegeven.
#   De formule is: temp = (temp_in_celsius * 9 / 5) + 32
# Vraag aan de gebruiker welke temperatuureenheid hij gebruikt. 
# Vraag vervolgens de temperatuur. 
# Bereken de overeenkomstige temperatuur en print deze af.

def geef_celsius(t_in_fahrenheit):
    temp = (t_in_fahrenheit-32)*5/9
    return temp

def geef_fahr(t_in_celsius):
    temp = (t_in_celsius *9/5)+32
    return temp

eenheid = input("Geef een eenheid C of F: ")
if eenheid.upper() == "C":
    t_in_celsius = float(input("Geef de temperatuur in C: "))
    temp = geef_fahr(t_in_celsius)
    print("De overeenkostige temperatuur is {0} graden Fahrenheit".format(round(temp,2)))
elif eenheid.upper() == "F":
    t_in_fahrenheit = float(input("Geef de temperatuur in F: "))
    temp = geef_celsius(t_in_fahrenheit)
    print("De overeenkostige temperatuur is {0} graden Celsius".format(round(temp,2)))
else:
    print("ongeldige eenheid")