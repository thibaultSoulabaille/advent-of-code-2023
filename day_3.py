import re
from utils.utils import open_input

DAY = 3

input_file = open_input(DAY, test=True)

# ---------- PART 1 ---------- #


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


def part_1() -> None:
    res = 0

    for idx, line in enumerate(input_file):
        prev_line = input_file[max(0, idx-1)]
        next_line = input_file[min(idx+1, len(input_file)-1)]

        res += get_line_score(
            acc_line=line,
            prev_line=prev_line,
            next_line=next_line
        )

    print(f'{res=}')


# ---------- PART 2 ---------- #

def part_2() -> None:
    res = 0
    print(f'{res=}')


if __name__ == "__main__":
    print("PART 1 >>>>>>>>>>")
    part_1()
    print("PART 2 >>>>>>>>>>")
    part_2()
