import numpy as np
from utils.utils import open_input

DAY = 14
TEST = False


def slide_column(column: str):
    column = column.replace('O', '1')
    column = column.replace('.', '0')
    column = column.split('#')
    # print(f'{column=}')

    slided_column = []
    for rocks_group in column:
        if len(rocks_group) > 0:
            slided_rocks = list(rocks_group)
            slided_rocks.sort()
            slided_rocks.reverse()
            slided_column.append(''.join(slided_rocks))
        slided_column.append('0')

    return ''.join(slided_column)[:-1]


def part_1(file: list) -> int:
    res = 0
    width, height = len(file), len(file[0])

    file_array = np.array([list(line) for line in file])
    file_array_t = file_array.T

    for column in file_array_t:
        slided_column = slide_column(''.join(column))

        for i in range(width):
            res += (width - i)*int(slided_column[i])

    return res


def part_2(file: list) -> int:
    res = 0
    return res


def main(test: bool) -> None:
    input_file = open_input(DAY, test=test, as_list=True)
    print(f'PART 1 >>>>>>>>>> {part_1(input_file)}')
    print(f'PART 2 >>>>>>>>>> {part_2(input_file)}')


if __name__ == "__main__":
    main(test=TEST)
