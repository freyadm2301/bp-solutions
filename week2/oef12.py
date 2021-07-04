# Schrijf een functie die een maandnummer binnenkrijgt. 
# Controleer of het getal tussen 1 en 12 ligt. 
# Geef de corresponderende maand terug. 
# Indien buiten het interval, geef je een foutboodschap terug. 
# Test de functie met meerdere maandnummers.

def maand(nummer):
    if 1 <= nummer <= 12:
        if nummer == 1:
            return 'Januari'
        elif nummer == 2:
            return 'Februari'
        elif nummer == 3:
            return 'Maart'
        elif nummer == 4:
            return 'April'
        elif nummer == 5:
            return 'Mei'
        elif nummer == 6:
            return 'Juni'
        elif nummer == 7:
            return 'Juli'
        elif nummer == 8:
            return 'Augustus'
        elif nummer == 9:
            return 'September'
        elif nummer == 10:
            return 'November'
        elif nummer == 11:
            return 'October'
        elif nummer == 12:
            return 'December'
    else:
        return "ongeldig maandnummer"

maandnummer = int(input('Geef een maandnummer: '))
print(maand(maandnummer))