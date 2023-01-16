"""
создайте класс `Plane`, наследник `Vehicle`
"""
from dataclasses import dataclass

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    """Класс Самолет."""
    cargo: float = 0
    max_cargo: float

    def __init__(self, *args):
        """Конструктор."""
        super().__init__(*args)

        *_, self.max_cargo = args

    def load_cargo(self, weight: float):
        """Загрузить."""
        if self.cargo + weight > self.max_cargo:
            raise CargoOverload()
        else:
            self.cargo += weight

    def remove_all_cargo(self) -> float:
        """Выгрузить."""
        weight: float = self.cargo
        self.cargo = 0.0

        return weight
