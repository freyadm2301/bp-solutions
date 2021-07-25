# Gebruik van dictionary
## Oef 3
Maak volgende 2 dictionaries aan. Ze stellen beide de verschillende studentenaantallen per opleidingsjaar voor.
- 'nmct' met de elementen {"1NMCT":131, "2NMCT":88, "3NMCT":77}
- 'devine' met de elementen {"1Devine": 123, "2Devine":98, "3Devine":55}

Geef een antwoord op onderstaande vragen d.m.v. een kort codevoorbeeld op bovenstaande dictionaries:
- *Wat is het effect van het print-commando op een dictionary?*
- *Hoe kan je een element uit de dictionary opvragen?*
- *Hoe voeg je een nieuw element aan de dictionary toe?*
- *Wat gebeurt er als een nieuw element met dezelfde key aan een dictionary wordt toegevoegd?*
- *Hoe controleer je of een key in een dictionary reeds in gebruik is?*
- *Hoe kan je een key (met value) uit een dictionary verwijderen? Wat als de key niet aanwezig is?*

## Oef 4
Maak nu één functie 'print-dictionary' die de verschillende elementen overloopt waarbij telkens key & value samen op één lijn worden afgeprint.
De functie heeft als parameters een naam (voor de dictionary) en de dictionary zelf.

## Oef 5
Maak een nieuwe lege dictionary 'Howest' aan.
Voeg de dictionaries uit oef 4 toe.

## Oef 6
Maak een methode 'voeg_nieuw_element_toe' aan die een nieuw element aan de dictionary toevoegd nadat er eerst gecontroleerd wordt of de key nog niet in gebruik is. Indien de key al in gebruik is, wordt er een foutboodschap afgeprint.
De methode heeft als parameters de key, de value en de dictionary zelf.

Test dit uit door aan dictionary Howest achtereenvolgens toe te voegen
- element met key '1IPO' met de waarde '51'
- element met key '1IPO' met de waarde '10'

print nadien telkens de dictionary Howest af (via methode uit oefening 4).

## Oef 7
Maak een functie 'geef_dict' die een dictionary teruggeeft waarbij de keys lopen van 1 tem 20 en de values steeds het kwadraat van de key zijn.

## Oef 8
Maak een functie ‘tel_voorkomen_woorden’ met als parameter een string. De functie geeft een dictionary terug waarbij de keys de verschillende woorden uit de zin zijn en de bijhorende values het aantal keer is dat het woord in de zin voorkomt. Print nadien de dictionary af.

## Oef 9
Maak een python applicatie die in staat is om de binnengekomen feedbackscores (van een evenement) te verwerken.
Hierbij wordt aan een medewerker gevraagd alle feedbackscores één voor één in te voeren.
De medewerker kan afsluiten met een lege score.
Op het einde worden de scores geteld en afgeprint.