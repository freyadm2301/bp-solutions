from model.Geboortedatum import Geboortedatum


def test_geboortedatums():
    # controle
    datum1 = Geboortedatum(25, 9, 1977)
    print(datum1)
    # datum1.dag = 31           #controle testen
    # print(datum1)

    datum2 = Geboortedatum(25, 9, 1977)
    if (datum1 == datum2):
        print("gelijk")
    else:
        print("niet gelijk")

   # print("Willekeurige lijst geboortedatums: ")
   # aantal = int(input("Hoeveel geboortedatums wenst u? "))
   # geboortedatums = Geboortedatum.genereer_lijst_verjaardagen(aantal)
    #index = 1
   # for datum in geboortedatums:
       #print("{0} : {1} ".format(index, datum))
       # index += 1

   # print("Totaal gecreëerde objecten van de klasse Geboortedatum: {0}".format(Geboortedatum.geef_aantal_geboortedatums()))


test_geboortedatums()