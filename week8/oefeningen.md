## Oef 1
Maak een klasse Speler die naast een naam en voornaam ook een individuele score bijhoudt.
Voorzie de klasse nu van:
- de gevraagde properties met de nodige inputvalidatie
- de klassieke methodes \_\_init__() en \_\_str__()

Breid nu deze klasse uit zodat ook de totale score van het volledige team kan opgevraagd worden:
dit is de som van alle individuele scores.
(Let op: deze teamscore is voor elke speler gelijk)
Voorzie een static-methode om deze teamscore terug te geven.
Test uit door verschillende objecten van deze klasse aan te maken.

## Oef 2
Maak een dataklasse Geboortedatum.
Zorg ervoor dat dag, maand en jaartal bijgehouden worden.
Voorzie nu zelf de klasse van:
- De gevraagde properties.
Bouw controles in wanneer dag/maand/jaartal gewijzigd worden.
- Programmeer de methode \_\_init__()
- Programmeer de methode \_\_str__()

Breid de klasse nu vervolgens uit:
- Hou het aantal gecreërde objecten van de klasse Geboortedatum bij.
- Maak een static methode om deze property op te vragen.
- Maak een static methode die een willekeurige geboortedatum genereert.
- Maak een static methode die een list van willekeurige geboortedatums genereert en terug geeft
- De parameter is het gewenste aantal.
- Integreer een methode die instaat om de gelijkheid tussen twee geboortedatums te controleren.
Bepaal eerst vooraf wanneer twee geboortedatums aan elkaar gelijk zijn.
(Tip: gebruik operator overloading!)
- Maak een (gewone) methode met als parameter een object Geboortedatum,
die controleert of beide op dezelfde dag verjaren (m.a.w. dag & maand zijn gelijk)

Test uit door verschillende objecten van deze klasse aan te maken.
Plaats deze test in een ander afzonderlijk python-bestand.
## Oef 3
We integreren vorige oefeningen in elkaar. Zorg ervoor dat van elke speler ook de geboortedatum
(object van de klasse Geboortedatum) wordt bijgehouden.
Print van elke aangemaakte speler nu ook zijn geboortedatum af.
## Oef 4
Maak een applicatie waarmee men de kamerbezetting van een hotel kan beheren.
Een receptionist zal je applicatie gebruiken om het kamerbeheer te doen.
Maak hiervoor de volgende klassen:
- Een klasse Hotelgast die de naam, voornaam en het adres moet bevatten.
- Een klasse Hotelkamer die het nummer en een list met gasten bijhoudt.
- Een klasse Hotel met een dictionary waarin de verschillende hotelkamers bijgehouden worden:

het kamernummer kan als key gebruikt worden.
Implementeer minimaal volgende methodes om:
- Alle vrije hotelkamers te printen
- Alle bezette hotelkamers te printen
- Info over een specifieke hotelkamer weer te geven
- Een reservatie te maken
- Een reservatie op te zoeken a.d.h.v. de naam van een gast
- De kamerbezetting te tonen

Implementeer alle methodes.
Test vervolgens alles voldoende uit.