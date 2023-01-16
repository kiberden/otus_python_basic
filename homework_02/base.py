from dataclasses import dataclass
from homework_02.exceptions import NotEnoughFuel, LowFuelError
from abc import ABC


@dataclass
class Vehicle(ABC):
    """Класс двигателя."""
    weight: float = 40
    started: bool = False
    fuel: float = 40
    fuel_consumption: float = 1.0

    def __init__(self, weight: int, fuel: int, fuel_consumption: float, *args):
        """Конструктор."""
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        """Завелись."""
        if not self.started:
            if self.fuel <= 0:
                raise LowFuelError("Low fuel error!")
            else:
                self.started = True

    def move(self, distance: float):
        """Поехали."""
        spent_fuel: float = distance * self.fuel_consumption

        if spent_fuel > self.fuel:
            raise NotEnoughFuel()
        else:
            self.fuel -= spent_fuel
