from utils.utils import open_input

DAY = 9


def get_next_element(sequence: list[int]) -> int:
    res = 0
    while any(sequence):
        res += sequence[-1]
        sequence = [
            sequence[i+1] - sequence[i] for i in range(len(sequence) - 1)
        ]
    return res


def part_1(file: list) -> int:
    res = 0
    for sequence in file:
        sequence = list(map(int, sequence.split()))
        res += get_next_element(sequence)
    return res


def part_2(file: list) -> int:
    res = 0
    for sequence in file:
        sequence = list(map(int, sequence.split()))
        sequence.reverse()
        res += get_next_element(sequence)
    return res


def main(test: bool) -> None:
    input_file = open_input(DAY, test=test, as_list=True)
    print(f'PART 1 >>>>>>>>>> {part_1(input_file)}')
    print(f'PART 2 >>>>>>>>>> {part_2(input_file)}')


if __name__ == "__main__":
    main(test=False)
