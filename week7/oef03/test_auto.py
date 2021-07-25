from model.Auto import Auto

mijn_auto = Auto("blauw", "Toyota", "benzine", "Starlet", 0)

print(mijn_auto.kleur)
print(mijn_auto.merk)
print(mijn_auto.brandstof)
print(mijn_auto.model)
print(mijn_auto.kmstand)
mijn_auto.rijden(50)
print(mijn_auto.kmstand)
print(mijn_auto)
