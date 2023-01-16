"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    """Исключение мало топлива."""
    pass


class NotEnoughFuel(Exception):
    """Исключение нет топлива."""
    pass


class CargoOverload(Exception):
    """Исключение перегруз."""
    pass
