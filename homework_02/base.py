from abc import ABC

from homework_02.exceptions import (LowFuelError,
                                    NotEnoughFuel)


class Vehicle(ABC):
    def __init__(self, weight=3000, fuel=40, fuel_consumption=1) -> None:
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError('Недостаточно топлива чтобы завести технику.')


    def move(self, distance):
        fuel_need = self.fuel_consumption * distance
        if fuel_need <= self.fuel:
            self.fuel -= fuel_need
        else:
            raise NotEnoughFuel('Недостаточно топлива для преодоления требуемой дистанции.')
