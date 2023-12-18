from math import lcm
from utils.utils import open_input


DAY = 8

position_trad = {
    "L": 0,
    "R": 1
}


def extract_info(file: str) -> (list, dict):
    path, network = file.split('\n\n')
    nodes = {
        node.split(' = ')[0]: node.split(' = ')[1][1:-1].split(', ') for node in network.split('\n')
    }
    return list(path), nodes


def part_1(file: str) -> int:
    path, nodes = extract_info(file)

    res = 0
    current = 'AAA'
    while current != 'ZZZ':
        for instr in path:
            current = nodes[current][position_trad[instr]]
            res += 1
    return res


def part_2(file) -> int:
    path, nodes = extract_info(file)
    res = 0

    current = [
        node for node in nodes.keys() if node[-1] == 'A'
    ]

    all_res = [0]*len(current)

    for idx, node in enumerate(current):
        res = 0
        while node[-1] != 'Z':
            for instr in path:
                node = nodes[node][position_trad[instr]]
                res += 1
        all_res[idx] = res

    return lcm(*all_res)


def main(test: bool) -> None:
    input_file = open_input(DAY, test=test, as_list=False)
    print(f'PART 1 >>>>>>>>>> {part_1(input_file)}')
    print(f'PART 2 >>>>>>>>>> {part_2(input_file)}')


if __name__ == "__main__":
    main(test=False)
