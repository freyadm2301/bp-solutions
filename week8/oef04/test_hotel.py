from model.Hotelgast import Hotelgast
from model.Hotelkamer import Hotelkamer

g1 = Hotelgast("Laprudence","Christophe","GKG")
g2 = Hotelgast("Walcarius","Stijn","GKG")
print(g1)
print(g2)
lijstje = [g1,g2]
k1 = Hotelkamer("A2", lijstje)
print(k1)
g3 = Hotelgast("Roobrouck","Dieter","GKG")
k1.voeg_gast_toe(g3)
print(k1)
print(k1.is_beschikbaar())
k1.check_out()
print(k1.is_beschikbaar())
k2 = Hotelkamer("A3")
print(k2.is_beschikbaar())
