# hou ook rekening met de geboortemaand en geboortedag om te verifiëren of iemand reeds 18 is.
import datetime
nu = datetime.datetime.now()
huidig_jaar = nu.year
huidige_maand = nu.month
huidige_dag = nu.day

jaar = int(input("Wat is uw geboortejaar? "))
maand = int(input("Wat is uw geboortemaand? "))
dag = int(input("Wat is uw geboortedag? "))

if jaar < huidig_jaar-18:
    print("Ok, u mag alcohol drinken.")
elif jaar == huidig_jaar-18:
    if maand < huidige_maand:
        print("Ok, je mag drinken")
    elif maand == huidige_maand:
        if dag <= huidige_dag:
            print("Ok, je mag drinken ")
        else:
            print("Sorry je bent nog geen 18, kom later eens terug.")
    elif maand > huidige_maand:
        print("Sorry je bent nog geen 18, kom later eens terug.")
elif jaar > huidig_jaar-18:
    print("Sorry je bent nog geen 18, kom later eens terug.")