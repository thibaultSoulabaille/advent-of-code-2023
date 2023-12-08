import re
from day import Day

DAY = 4


def get_line_score(line: str) -> int:
    card = line.split(':')[1]
    win_nb, have_nb = [
        re.findall('\d+', nb_list) for nb_list in card.split('|')
    ]
    score = len(set(win_nb).intersection(have_nb))
    if score > 0:
        return 2**(score - 1)
    return 0


class Day4(Day):
    def __init__(self, day: int, test: bool = False) -> None:
        super().__init__(day, test)

    def part_1(self) -> int:
        return sum(list(map(get_line_score, self.input_file)))

    def part_2(self) -> int:
        return 0


if __name__ == "__main__":
    day_4 = Day4(DAY)
    print(f'{day_4.part_1()=}')
    print(f'{day_4.part_2()=}')
