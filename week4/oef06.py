# Maak een functie ‘kies_element’ aan met als parameter een list. 
# De functie kiest een willekeurig element uit de doorgegeven list en geeft deze terug. 
# Test deze functie met
# - een list met strings, nl. de verschillende maanden
# - een list met getallen
import random
def kies_element(list_elementen):
    element = random.choice(list_elementen)
    return element
maanden = ["januari","februari","maart","april","mei","juni","juli","augustus","september","oktober","november","december"]
list_get = [9,7,15,84,65,98,74,62]
print("De gekozen maand is {0}".format(kies_element(maanden)))
print("Het gekozen getal is {0}.".format(kies_element(list_get)))

#versie 2

def kies_element2(een_lijst):
    gekozen_element = ""
    lengte = len(een_lijst)
    willekeurige_index = random.randint(0,len(een_lijst)-1)
    gekozen_element = een_lijst[willekeurige_index]
    return gekozen_element

print('De gekozen maand is',kies_element2(maanden))
print('Het gekozen getal is',kies_element2(list_get))