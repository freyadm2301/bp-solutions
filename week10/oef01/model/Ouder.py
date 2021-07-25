from model.Persoon import Persoon
from model.Student import Student

class Ouder(Persoon):
    def __init__(self, par_naam, par_voornaam, par_geb_jaar = 1970, par_list_met_kinderen = []):
        Persoon.__init__(self, par_naam, par_voornaam, par_geb_jaar)
        self.__studenten = par_list_met_kinderen


    @property
    def studenten(self):
        return self.__studenten

    def voeg_student_toe(self, nieuwe_student):
        if isinstance(nieuwe_student, Student):
            #dankzij eq in student controle of nieuw oject er al in zit of niet
            if nieuwe_student in self.__studenten:
                print('Niet toegevoegd, staat er al in.')
            else:
                self.__studenten.append(nieuwe_student)
        else:
            print('Fout')

    def geef_info_studenten(self):
        uitkomst = 'Mijn kind(eren): '
        for student in self.studenten:
            uitkomst += student.voornaam + '\n'
        return '{0} \n{1}'.format(self.__str__(), uitkomst)
    def __str__(self):
        return 'OUDER: {0}'.format(Persoon.__str__(self))

    def geef_opleidingen_studenten(self):
        Opleidingen = []
        OP = []
        for student in self.studenten:
            Opleidingen.append(student.opleiding)

        for opleiding in Opleidingen:
            if opleiding not in OP:
                OP.append(opleiding)

        return print('De verschillende opleidingen van de kinderen zijn: {0}'.format(OP))
