# Maak telkens 2 variabelen (datatype integer) in volgende formaat aan:
# - Decimaal
# - Octaal
# - Hexadecimaal
# - Binair
# Print beide getallen in bovenstaande formaat af. Print nadien ook de som af.

getal1 = int(input("geef een eerste getal: "))
getal2 = int(input("geef een tweede getal: "))

dec1 = float(getal1)
dec2 = float(getal2)
oct1 = oct(getal1)
oct2 = oct(getal2)
hex1 = hex(getal1)
hex2 = hex(getal2)
bin1 = bin(getal1)
bin2 = bin(getal2)

som = getal1 + getal2
print('Het getal is {0}\n - Decimaal: {1}\n - Octaal: {2}\n - Hexadecimaal: {3}\n - Binair: {4}'.format(getal1,dec1,oct1,hex1,bin1))
print('Het getal is {0}\n - Decimaal: {1}\n - Octaal: {2}\n - Hexadecimaal: {3}\n - Binair: {4}'.format(getal2,dec2,oct2,hex2,bin2))
print('De som van deze getallen is {0}'.format(som))