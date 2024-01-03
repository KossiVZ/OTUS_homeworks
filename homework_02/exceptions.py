"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class CargoOverload(Exception):
    pass

class LowFuelError(Exception):
    pass

class NotEnoughFuel(Exception):
    pass

