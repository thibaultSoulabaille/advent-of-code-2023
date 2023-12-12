from typing import Any


def open_input(day: int, test: bool = False, as_list: bool = True) -> Any:
    if test:
        f_name = f'input/test/day_{day}_test.txt'
    else:
        f_name = f'input/day_{day}.txt'
    if as_list:
        return open(f_name).read().splitlines()
    return open(f_name).read()
