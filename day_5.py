from utils.utils import open_input

DAY = 5


def extract_map(block: str) -> list:
    return [
        list(map(int, range_n.split(' '))) for range_n in block.split('\n')[1:]
    ]


def get_map_result(source: int, map_: list) -> int:
    for dst, src, step in map_:
        if src <= source <= src + step:
            return dst + source - src
    return source


def get_seed_location(seed: int, maps: list) -> int:
    res = seed
    for map_ in maps:
        res = get_map_result(res, map_)
    return res


def part_1(file: str) -> int:
    file_blocks = file.split('\n\n')
    seeds = list(map(
        int, file_blocks[0].split(':')[1].split()
    ))
    maps = [extract_map(block) for block in file_blocks[1:]]

    locations = []
    for seed in seeds:
        locations.append(get_seed_location(seed, maps))

    return min(locations)


def part_2(file) -> int:
    return 0


def main(test: bool) -> None:
    input_file = open_input(DAY, test=test, as_list=False)

    print(f'PART 1 >>>>>>>>>> {part_1(input_file)}')
    print(f'PART 2 >>>>>>>>>> {part_2(input_file)}')


if __name__ == "__main__":
    main(test=False)
