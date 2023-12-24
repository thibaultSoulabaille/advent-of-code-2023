import re
from utils.utils import open_input

DAY = 1
TEST = False


def part_1(file: str) -> int:
    res = 0

    for line in file:
        line_strip = line.split()[0]
        is_int = list(map(lambda x: x.isnumeric(), line_strip))
        first_int = line_strip[is_int.index(True)]
        is_int.reverse()
        last_int = line_strip[len(line_strip) - 1 - is_int.index(True)]

        res += int(f"{first_int}{last_int}")

    return res


def part_2(file: str) -> int:
    res = 0
    str_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    for line in file:
        numbers = {}

        for digit_str, digit_int in str_digits.items():
            find_int = re.finditer(digit_int, line)
            find_str = re.finditer(digit_str, line)
            if find_int is not None:
                for f in find_int:
                    numbers[f.start()] = digit_int
            if find_str is not None:
                for f in find_str:
                    numbers[f.start()] = digit_int

        sorted_pos = list(numbers.keys())
        sorted_pos.sort()
        sorted_numbers = [numbers[i] for i in sorted_pos]

        res += int(f"{sorted_numbers[0]}{sorted_numbers[-1]}")
    return res


def main(test: bool) -> None:
    input_file = open_input(DAY, test=test, as_list=True)

    print(f'PART 1 >>>>>>>>>> {part_1(input_file)}')
    print(f'PART 2 >>>>>>>>>> {part_2(input_file)}')


if __name__ == "__main__":
    main(test=TEST)
