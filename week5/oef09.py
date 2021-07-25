# Maak een python applicatie die in staat is om de binnengekomen feedbackscores (van een evenement) te verwerken.
# Hierbij wordt aan een medewerker gevraagd alle feedbackscores één voor één in te voeren.
# De medewerker kan afsluiten met een lege score.
# Op het einde worden de scores geteld en afgeprint.

def get_scores():
    print("Geef de verschillende evaluatiecijfers door (sluit af met lege waarde)")
    print("Uitmuntend: 5, Zeer goed: 4, Goed: 3, Voldoende: 2, Onvoldoende: 1, Zwak: 0")
    scores = {"5":0, "4":0, "3":0, "2":0, "1":0, "0":0}
    cijfer = input("Geef de nieuwe evaluatiescore op: ")
    while cijfer != "":
        if cijfer == "5":
            scores["5"] += 1
        elif cijfer == "4":
            scores["4"] += 1
        elif cijfer == "3":
            scores["3"] += 1
        elif cijfer == "2":
            scores["2"] += 1
        elif cijfer == "1":
            scores["1"] += 1
        elif cijfer == "0":
            scores["0"] += 1
        cijfer = input("Geef de nieuwe evaluatiescore op: ")
    print("De gegevens zijn verwerkt. Dit is het resultaat")
    for cijfer in scores.keys():
        print("score: {0} -> aantal: {1}".format(cijfer, scores[cijfer]))

get_scores()
