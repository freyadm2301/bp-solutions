## Oef 1
Werk verder op de demo uit de theorieles.(Zie ook bronmateriaal bij deze opgave)
Voeg de klasse ‘Ouder’ toe die erft van de klasse Persoon.
Deze klasse krijgt één extra attribuut, nl. een list van studenten(we gaan er voor de eenvoud vanuit dat alle kinderen studenten zijn).
Werk deze klasse nu systematisch uit.
Test regelmatig.
- Implementeer de methodes \_\_init__( ) & \_\_str__( )
- Een property-methode ‘studenten’die de list van studenten teruggeeft.
Een setter-methode hoeft niet toegevoegd te worden.
- Een methode ‘voeg_student_toe’ langswaar een student kan toegevoegd worden.
Controleer steeds of de student nog niet in de list aanwezig is.
Welke methode wordt voor deze controlegebruikt?
- Een methode ‘geef_info_studenten’die een string teruggeeft waarin zowel de info van de ouder als de info over elke student verwerkt zit.
- Een methode ‘geef_opleidingen_studenten’die een list met de namen van de opleidingen van de kinderen teruggeeft.
Dubbels mogen niet voorkomen.

Test alle methodes uit.
Maak finaal ook een nieuw object van de klasse Auto aan waarbij de ouder als eigenaar wordt ingesteld.
Print de \_\_str__() van de klasse Auto af.
Dient de klasse Auto aangepast te worden?
Waarom wel/niet?
Opmerking: Je kan de test-methode in het bronmateriaal van deze oefening gebruiken.
## Oef 2
Het taxibedrijf NMCT@car heeft sinds kort,
naast drie wagens ook twee lichte vrachtwagens rondrijden.
Van elk voertuig wordt standaard het bouwjaar, het merk, het aantal km en de reisbestemming bijgehouden.
Voor de wagens in het bijzonder wordt naast het maximum aantal passagierplaatsen ook continue het aantal vervoerde personen bijgehouden.
Analoog voor de lichte vrachtwagens wordt naast het maximaal toegelaten laadvermogen ook continue  het  gewicht van de vervoerde vracht bijgehouden.
Vanuit een monitorcentrum wenst men een applicatie die de status van elk voertuig kan weergeven en aanpassen.

Maak de klasse Voertuig, Personenwagen en Vrachtwagen.
Welke relatie bestaat tussen deze klasses?
1. Klasse Voertuig
Properties (incl. resp instantieattributen)*: merk, bouwjaar, kmstand, reisbestemming, id
Methodes: \_\_init__, \_\_del__, \_\_str__, \_\_lt__, geef_detail_info(),...
Static-methodes: geef_aantal_voertuigen()
2. Klasse Vrachtwagen erft van de klasse Voertuig
Extra properties (incl. resp instantieattributen)*: vracht, max_laad_vermogen
Methodes: \_\_init__, \_\_str__, geef_detail_info()
3. Klasse Personenwagen erft van de klasse Voertuig
Extra properties(incl. resp instantieattributen)*:max_aantal_zitplaatsen, aantal_personen
Methodes:\_\_init__,\_\_str__, geef_detail_info()

Extra opmerkingen:
- Voorzie inputvalidatie in de property-setters.
Bij foutieve input geef je een ValueError terug.
- Voorzie de klasse Voertuig van een static-attribuut ‘__aantal_voertuigen’(die het aantal gecreëerde objecten van deze klasse bijhoudt)
en een static-methode‘geef_aantal_voertuigen’die het aantal teruggeeft.
- Voorzie de klasse Voertuig ook van een property id: dit is een uniek identificatienummer.
Dit nummer wordt bij het aanmaken van het object ingesteld.
Gebruik hiervoor de‘uuid.uuid4()’ (UUID = Universally Unique Identifier)self.__id = uuid.uuid4()
- Voorzie de klasse Voertuig van een methode ‘geef_detail_info’.
Werk deze methode ook in de klassen Personenwagen en Vrachtwagen uit.
- Maak in de methode \_\_str__()  van de klasse Personenwagen en Vrachtwagen gebruik van de methode \_\_str__() uit de klasse Voertuig.