import re
from day import Day

DAY = 3


def extract_numbers(line: str) -> list[str]:
    return re.findall('\d+', line)


def check_number(number_idx: int, number_len: int, lines: list[str]) -> bool:
    for line in lines:
        line_clean = re.sub('[0-9.]', '0', line)
        line_clean = re.sub('[^0]', '1', line_clean)

        line_list = list(map(int, list(line_clean)))

        if sum(line_list[max(0, number_idx-1):min(number_idx+number_len+1, len(line_list))]) > 0:
            return True

    return False


def get_line_score(acc_line: str, prev_line: str, next_line: str) -> int:
    line_score = 0
    numbers = extract_numbers(acc_line)

    for number in numbers:
        number_idx = acc_line.find(number)
        number_len = len(number)
        if check_number(number_idx, number_len, [prev_line, acc_line, next_line]):
            line_score += int(number)

        acc_line = acc_line.replace(number, '.'*number_len, 1)

    return line_score


class Day3(Day):
    def __init__(self, day: int, test: bool = False) -> None:
        super().__init__(day, test)

    def part_1(self) -> int:
        res = 0

        for idx, line in enumerate(self.input_file):
            prev_line = self.input_file[max(0, idx - 1)]
            next_line = self.input_file[min(idx + 1, len(self.input_file) - 1)]

            res += get_line_score(
                acc_line=line,
                prev_line=prev_line,
                next_line=next_line
            )

        return res

    def part_2(self) -> int:
        return 0


if __name__ == "__main__":
    day_3 = Day3(DAY)
    print(f'{day_3.part_1()=}')
    print(f'{day_3.part_2()=}')
