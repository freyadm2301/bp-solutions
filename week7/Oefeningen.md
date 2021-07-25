# Object Georiënteerd Programmeren
## Oef 1
Maak een dataklasse Boek.
Wat zijn de kenmerken waarmee een boek zich kan identificeren?
Codeer nu deze dataklasse:
- Voorzie de klasse van de nodige attributen en properties.
- Programmeer de methode \_\_init__()
- Programmeer de methode \_\_str__()

Test uit door verschillende objecten van deze klasse aan te maken.
Gebruik hiervoor een afzonderlijk bestand.

## Oef 2
Bestudeer het bronbestand bieren.csv.
Door welke zaken wordt een bier gekenmerkt?
Maak nu een dataklasse Bier.
- Voorzie de klasse van de nodige attributen en properties.
    - In de setter wordt de nieuwe waarde  gecontroleerd: een lege string wordt naar ‘onbekend’ omgezet.
    - Het alcoholpercentage moet tussen 0 en 100 liggen.
- Programmeer de methode \_\_init__()
- Programmeer de methode \_\_str__()

Maak verschillende bieren aan. Wijzig nadien de attributen via de setter-methodes. Controleer of de functionaliteit in orde is.

## Oef 3
Maak een dataklasse Auto waarbij volgende zaken worden bijgehouden:
kleur, merk, brandstof, model, km-stand.
Hoe kan je er voor zorgen dat enkel de attributen km-stand en kleur nadien gewijzigd kunnen worden?
Voeg ook een methode ‘rijden’ met de parameter extra_km toe:
hiermee wordt de km-stand van de auto verhoogd.
Test alles uit: maak een list aan met verschillende voertuigen. Laat vervolgens elk voertuig uit de list een random afstand afleggen. Print nadien van elk voertuig de km-stand af.

## Oef 4
We wensen van elk wiel de straal en het aantal omwentelingen bijhouden.
Hiervoor maken we een klasse Meetwiel met de instantie-attributen ‘straal’en‘omwentelingen’(default-waarde:0).
Volgend stappenplan kan gevolgd worden:
- Voorzie de klasse van de nodige attributen en bijhorende properties.
- Voorzie 2 extra property-methodes:
    - Programmeer de property-methode omtrek(): deze geeft de omtrek van het wiel terug
    - Programmeer de property-methode afstand(): deze geeft de afgelegde afstand ifv de het aantal omwentelingen en de omtrek van het meetwiel terug.
- Programmeer de methode \_\_init__()
- Programmeer de methode \_\_str__()

Test voldoende uit door verschillende objecten van deze klasse aan te maken. Vraag tenslotte aan de gebruiker meerdere extra omwentelingen voor een wiel op. Sluit af met ‘c’ Print nadien de afgelegde afstand opnieuw af.

## Oef 5
Maak een dataklasse Winkelkar dat als private attribuut een list van producten (String) bijhoudt.
Voorzie de klasse van volgende methodes:
- Programmeer de methode \_\_init__()
- Programmeer de methode \_\_str__()
- ‘Read-only’ property-methode ‘producten’ dat de lijst terug geeft.
- Methode ‘voeg_product_toe(nieuw_product)’ dat een nieuw productaan het winkelkarretje toevoegt.
- Methode ‘verwijder_product(product)’ dat een product uit het winkelkarretje verwijdert.
- Zorg ervoor dat de +-operator toegepast kan worden:
    - zodat twee winkelkarretjes bij elkaar kunnen opgeteld worden en een nieuw winkelkarretje opleveren (welke methode moet hiervoor toegevoegd worden?)
    - zodat het bestaande winkelkarretje uitgebreid wordt met de producten uit een andere winkelkarretje (welke methode moet hiervoor toegevoegd worden?)

Test alles uit:
- Maak 2 winkelkarrtjes aan. Voeg verschillende producten aan elk toe. Print nadien beide af.
- Tel beide winkelkarrtejes op via de plus-operator. Print resultaat af.