"""
создайте класс `Car`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    """Класс машина."""
    engine: Engine

    def set_engine(self, engine: Engine):
        """Установка двигателя."""
        self.engine = engine
