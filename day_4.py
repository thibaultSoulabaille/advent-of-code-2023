import re
from day import Day

DAY = 4


def get_line_score(line: str) -> int:
    score = get_n_matching_numbers(line)
    if score > 0:
        return 2**(score - 1)
    return 0


def get_n_matching_numbers(line: str) -> int:
    card = line.split(':')[1]
    win_nb, have_nb = [
        re.findall('\d+', nb_list) for nb_list in card.split('|')
    ]
    return len(set(win_nb).intersection(have_nb))


class Day4(Day):
    def __init__(self, day: int, test: bool = False) -> None:
        super().__init__(day, test)

    def part_1(self) -> int:
        return sum(list(map(get_line_score, self.input_file)))

    def part_2(self) -> int:
        n_lines = len(self.input_file)
        res = [1]*n_lines
        for i, line in enumerate(self.input_file):
            res_line = get_n_matching_numbers(line)
            for j in range(res_line):
                idx = i+j+1
                if idx >= n_lines:
                    break
                res[i+j+1] += res[i]
        return sum(res)


if __name__ == "__main__":
    day_4 = Day4(DAY)
    print(f'{day_4.part_1()=}')
    print(f'{day_4.part_2()=}')
