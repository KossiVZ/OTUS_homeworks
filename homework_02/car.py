"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle

class Car(Vehicle):
    def __init__(self, weight=3000, fuel=40, fuel_consumption=1) -> None:
        super().__init__(weight, fuel, fuel_consumption)
    
    def set_engine(self, engine):
        self.engine = engine
        return self