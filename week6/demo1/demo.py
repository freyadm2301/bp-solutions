#wegschrijven namen
def schrijf_naam_weg(lst_namen):
    #open
    mijn_bestand = open('week6/demo1/namen.txt','w')
    #actie
    #mijn_bestand.write('Jan')
    for naam in lst_namen:
        mijn_bestand.write(naam + "\n")
    #sluiten
    mijn_bestand.close()

lst = ['Karel', 'Sandrine', 'Kris']
schrijf_naam_weg(lst)

def lees_namen_in():
    #open
    fo = open('week6/demo1/namen.txt','r') #r staat voor lezen
    #actie
    lijn = fo.readline().rstrip('\n')
    while lijn != '':
        print(lijn)
        lijn = fo.readline().rstrip('\n')
    #sluiten
    fo.close()

lees_namen_in()