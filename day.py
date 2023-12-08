from abc import ABC, abstractmethod
from utils.utils import open_input


class Day(ABC):
    def __init__(self, day: int, test: bool = False) -> None:
        self.input_file = open_input(day, test=test)

    @abstractmethod
    def part_1(self) -> int:
        return 0

    @abstractmethod
    def part_2(self) -> int:
        return 0
