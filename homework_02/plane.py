"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

import os


class Plane(Vehicle):
    def __init__(self, weight=3000, fuel=40, fuel_consumption=1, max_cargo=10000) -> None:
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0
    
    def load_cargo(self, load):
        new_cargo = self.cargo + load
        if  new_cargo <= self.max_cargo:
            self.cargo = new_cargo
        else:
            raise CargoOverload('Транспортное средство перегружено.')

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
    
print(os.getcwd())