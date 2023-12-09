import re
from day import Day

DAY = 2


def extract_nb_colors(line: str) -> list:
    return [
        color.split() for color in re.findall('\d+ [a-z]+', line)
    ]


class Day2(Day):
    def __init__(self, day: int, test: bool = False) -> None:
        super().__init__(day, test)
        self.bag = {
            'red': 12,
            'green': 13,
            'blue': 14
        }
        self.bag_total = sum(self.bag.values())

    def _check_line(self, line: str) -> bool:
        n_colors = extract_nb_colors(line)

        for color, n in self.bag.items():
            max_color = max([
                int(val[0]) for val in n_colors if val[1] == color
            ])
            if max_color > n:
                return False

        games = line.replace(' ', '').split(':')[1].split(';')
        sum_game = [
            sum(map(int, re.findall('\d+', game))) for game in games
        ]

        if max(sum_game) > self.bag_total:
            return False
        return True

    def get_min_game_score(self, line: str) -> int:
        n_colors = extract_nb_colors(line)

        score = 1
        for color, n in self.bag.items():
            max_color = max([
                int(val[0]) for val in n_colors if val[1] == color
            ])
            score = score * max_color
        return score

    def part_1(self) -> int:
        res = 0
        for i, line in enumerate(self.input_file):
            if self._check_line(line):
                res += i + 1
        return res

    def part_2(self) -> int:
        res = 0
        for line in self.input_file:
            res += self.get_min_game_score(line)
        return res


if __name__ == "__main__":
    day_2 = Day2(DAY)
    print(f'{day_2.part_1()=}')
    print(f'{day_2.part_2()=}')
