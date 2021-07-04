# Schrijf een functie ‘printWelkom’ die twee strings als parameters heeft: naam en groep. 
# Zorg ervoor dat de parametergroep een defaultwaarde ‘NMCT @ Athena’ krijgt.
# Print een welkomstbericht af waarin naam & groep vermeld staan. 
# Test de functie voldoende (zowel met 1 als 2 argumenten)

def printwelkom(een_naam, een_groep = "NMCT @ Athena"):
    print("Welkom {0}, je zit in {1}".format(een_naam,een_groep))

printwelkom("Freya")
printwelkom("Freya","1MCT1")