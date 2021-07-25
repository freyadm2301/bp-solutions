from model.Speler import Speler

def test_spelers():
    sp1 = Speler("Stijn", "Walcarius", 10)
    sp2 = Speler("Dieter", "Roobrouck", 36)
    sp3 = Speler("Christophe", "Laprudence", 24)
    sp4 = Speler("Johan", "Vannieuwenhuyse", 72)

    list_spelers = [sp1, sp2, sp3, sp4]

    for speler in list_spelers:
        print(speler)


    print("Team score: {0}".format( Speler.score_team()))
    print("score speler 1 aanpassen naar 20")
    sp1.score = 20
    print("Team score: {0}".format( Speler.score_team()))

    print("speler 1 verwijderen")
    del(sp1)
    # del(list_spelers[0])
    print("Team score: {0}".format( Speler.score_team()))



test_spelers()