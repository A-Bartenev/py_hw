"""в модуле plane создайте класс Plane
класс Plane должен быть наследником Vehicle
добавьте атрибуты cargo и max_cargo классу Plane
добавьте max_cargo в инициализатор (переопределите родительский)
объявите метод load_cargo, который принимает число, проверяет, что в сумме с текущим cargo не
будет перегруза, и обновляет значение, в ином случае выкидывает исключение exceptions.CargoOverload
объявите метод remove_all_cargo, который обнуляет значение cargo и возвращает значение cargo, которое было до обнуления.
"""

from exceptions import *
from base import Vehicle
class Plan(Vehicle):
    cargo = 0
    def __init__(self,max_cargo=0):
        super().__init__(self)
        self.max_cargo = max_cargo
    def load_cargo(self, brutto):
            if self.cargo+brutto<self.max_cargo:
                self.cargo+=brutto
            else:
                raise CargoOverload('перегруз')
    def remove_all_cargo(self):
        self.cargo_drop=self.cargo
        self.cargo=0
        return self.cargo_drop

if __name__=='__main__':
    pass