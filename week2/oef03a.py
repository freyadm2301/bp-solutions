# Vraag aan de gebruiker wat zijn geboortejaar is. Indien hij nog geen 18 is, print dan ook een gepaste melding af.
import datetime
nu = datetime.datetime.now()
huidig_jaar = nu.year
huidige_maand = nu.month
huidige_dag = nu.day

jaar = int(input("Wat is uw geboortejaar? "))

if jaar < huidig_jaar-18:
    print("Ok, u mag alcohol drinken.")
elif jaar == huidig_jaar-18:
    print("Ok, u mag alcohol drinken.")
elif jaar > huidig_jaar-18:
    print("U bent nog geen 18!\nKom volgend jaar terug...")