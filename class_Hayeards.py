from class_Employees import *


class Hayeard(Employes):
    number_of_hayeards = 0
    hayeard_objects = []

    def __init__(self, f_n, l_n, i_d, phone, adreass, b_d, job, manager):
        super(Hayeard, self).__init__(f_n, l_n, i_d, phone, adreass, b_d, job)
        self.manager = manager
        Hayeard.hayeard_objects.append(self)
        manager.add_hayeard(self)
        Hayeard.number_of_hayeards += 1

    def change_menager(self, manager, new_menager):
        manager.remove_hayeard(self)
        self.manager = new_menager
        new_menager.add_hayeard(self)
        return f'{self.full_name()}\'s menager is now: {self.manager.full_name()}'
