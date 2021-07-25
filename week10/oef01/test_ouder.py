from model.Ouder import Ouder
from model.Student import Student

def test1():
    nieuwe_ouder = Ouder('Laprudence', 'Christophe', 1884)
    k1 = Student('Walcarius', 'Stijn', 124, 'MCT', 2000)
    k2 = Student('Walcarius', 'Fien', 1244, 'MCT', 2000)
    nieuwe_ouder.voeg_student_toe(k1)
    nieuwe_ouder.voeg_student_toe(k2)
    #print(nieuwe_ouder)

    print(nieuwe_ouder.geef_info_studenten())
    print(nieuwe_ouder.geef_opleidingen_studenten())
test1()