# Maak één list aan met de dagen van de week. Gebruik het printcommando in één codelijn volgende af te printen:
# - enkel de werkdagen van de week
# - de weekenddagen van de week
# - de onpare dagen van de week
# - de pare dagen van de week

list_dagen= ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag","zaterdag", "zondag"]
werkdagen = list_dagen[0:5]
weekenddagen = list_dagen[-2:]
onpare_dagen = list_dagen[1:7:2]
pare_dagen = list_dagen[0:7:2]
print(werkdagen)
print(weekenddagen)
print(onpare_dagen)
print(pare_dagen)