"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass
class Engine:
    """Класс Двигатель."""
    volume: float
    pistons: int
