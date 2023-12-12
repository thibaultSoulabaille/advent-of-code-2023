import math
from utils.utils import open_input

DAY = 6


def get_poly_roots(a: int, b: int, c: int) -> tuple[float, float]:
    delta = math.sqrt(b**2 - 4*a*c)
    root_0 = (-1*b + delta)/(2*a)
    root_1 = (-1*b - delta)/(2*a)
    return root_0, root_1


def get_bounds_from_roots(roots: tuple[float, float]):
    r_0, r_1 = sorted(roots)
    if int(r_0) == r_0:
        r_0 = int(r_0 + 1)
    else:
        r_0 = int(r_0) + 1

    if int(r_1) == r_1:
        r_1 = int(r_1 - 1)
    else:
        r_1 = int(r_1)

    return r_0, r_1


def part_1(file: str) -> int:
    times, distances = [line.split()[1:] for line in file]
    roots = [
        get_bounds_from_roots(get_poly_roots(-1, int(t), -1*int(d))) for (t, d) in zip(times, distances)
    ]
    return math.prod([
        abs(r_0 - r_1) + 1 for (r_0, r_1) in roots
    ])


def part_2(file) -> int:
    time_, distance = [
        int(line.split(':')[1].replace(' ', '')) for line in file
    ]
    r_0, r_1 = get_bounds_from_roots(get_poly_roots(-1, time_, -1*int(distance)))
    return abs(r_0 - r_1) + 1


def main(test: bool) -> None:
    input_file = open_input(DAY, test=test, as_list=True)
    print(f'PART 1 >>>>>>>>>> {part_1(input_file)}')
    print(f'PART 2 >>>>>>>>>> {part_2(input_file)}')


if __name__ == "__main__":
    main(test=False)
