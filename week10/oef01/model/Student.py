from model.Persoon import Persoon
class Student(Persoon):
    def __init__(self,par_naam, par_voornaam, par_student_nr, par_opleiding, par_geboortedatum = 2000):
        # Ga eerst naar PARENT CLASS
        Persoon.__init__(self, par_naam, par_voornaam,par_geboortedatum)
        self.opleiding = par_opleiding
        self.student_nr = par_student_nr

    @property
    def student_nr(self):
        return self.__student_nr

    @student_nr.setter
    def student_nr(self, value):
        self.__student_nr =value

    @property
    def opleiding(self):
        return self.__opleiding

    @opleiding.setter
    def opleiding(self, value):
        self.__opleiding = value

    def __str__(self):
        return "STUDENT {0} en nr {1}".format(super().__str__(), self.student_nr)

    def __eq__(self, other):
        if self.student_nr == other.student_nr:
            return True
        else:
            return False
