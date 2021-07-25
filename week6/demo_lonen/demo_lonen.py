def inlezen_lonen():
    #openen
    fo = open('week6/demo_lonen/lonenlijst.csv','r')
    #inlezen
    lijn = fo.readline().rstrip('\n') #sla titel over
    lijn = fo.readline().rstrip('\n')
    while lijn != '':
        lst_item_el = lijn.split(';')
        loon = float(lst_item_el[1])
        nieuw_loon = 1.1 * loon
        print("Naam: {0} - {1} nieuwe loon {2}".format(lst_item_el[0], lst_item_el[1],nieuw_loon))
        lijn = fo.readline().rstrip('\n')
    #sluiten
    fo.close()

inlezen_lonen()

def gemiddelde_leeftijd():
    #open
    fo = open('week6/demo_lonen/lonenlijst.csv','r')
    #inlezen
    lijn = fo.readline().rstrip('\n') #sla titel over
    lijn = fo.readline().rstrip('\n')
    som = 0
    aantal = 0
    while lijn != '':
        lst_item_el = lijn.split(';')
        leeftijd = int(lst_item_el[2])
        som += leeftijd
        aantal += 1
        lijn = fo.readline().rstrip('\n')
    #sluiten
    fo.close()
    #return uitkomst
    gem_leeftijd = som/aantal
    return gem_leeftijd

gem = gemiddelde_leeftijd()
print('De gemiddelde leeftijd is {0}'.format(gem))