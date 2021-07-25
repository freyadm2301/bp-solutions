from model.Meetwiel import Meetwiel

mijn_wiel = Meetwiel(2, 1)
print(mijn_wiel)
par_aantal = input('Geef het aantal omwenteling of sluit af met c: ')
mijn_wiel.doe_extra_omwentelingen(par_aantal)