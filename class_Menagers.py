from class_Employees import *


class Menagers(Employes):
    number_of_menagers = 0
    menagers_objects = []

    def __init__(self, f_n, l_n, i_d, phone, adreass, b_d, job):
        super(Menagers, self).__init__(f_n, l_n, i_d, phone, adreass, b_d, job)
        self.hayeard = []
        Menagers.menagers_objects.append(self)
        Menagers.number_of_menagers += 1

    def add_hayeard(self, employe):
        if employe in self.hayeard:
            return f'error, the hayeard id:{employe.i_d} is already asined to the menager {self.full_name()}'
        else:
            self.hayeard.append(employe)
            return f'the hayeard id:{employe.i_d} is now add to the menager {self.full_name()}'

    def remove_hayeard(self, employe):
        if employe in self.hayeard:
            self.hayeard.remove(employe)
            return f'the hayeard id:{employe.i_d} removed from the menager {self.full_name()}'
        else:
            return f'error, the hayeard id:{employe.i_d} is not under the menager {self.full_name()} view'

    def get_hayeards_info(self):
        hayeard_ditels = {h.i_d: {'f_n': h.f_n, 'l_n': h.l_n, 'i_d': h.i_d, 'phone': h.phone, 'adress': h.adreass}
                          for h in self.hayeard}
        return hayeard_ditels
