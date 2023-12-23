from utils.utils import open_input

DAY = 15
TEST = False


def hash_(input_: str) -> int:
    res = 0
    for char in input_:
        res = 17*(res + ord(char)) % 256
    return res


def part_1(file: str) -> int:
    res = 0
    steps = file.split(',')
    for step in steps:
        res += hash_(step)
    return res


def part_2(file: str) -> int:
    boxes = [{} for _ in range(256)]
    lenses = {}
    steps = file.split(',')

    for step in steps:
        if '-' in step:
            label = step[:-1]
            box_idx = hash_(label)
            if label in boxes[box_idx].keys():
                boxes[box_idx].pop(label)
        else:
            label, focal = step.split('=')
            box_idx = hash_(label)
            boxes[box_idx][label] = int(focal)

    for idx, box in enumerate(boxes):
        for i, lens in enumerate(box.items()):
            key, value = lens
            lenses[key] = (idx + 1) * (i + 1) * value

    return sum(lenses.values())


def main(test: bool) -> None:
    input_file = open_input(DAY, test=test, as_list=False)
    print(f'PART 1 >>>>>>>>>> {part_1(input_file)}')
    print(f'PART 2 >>>>>>>>>> {part_2(input_file)}')


if __name__ == "__main__":
    main(test=TEST)
