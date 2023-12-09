def open_input(day: int, test: bool = False) -> list[str]:
    if test:
        f_name = f'input/test/day_{day}_test.txt'
    else:
        f_name = f'input/day_{day}.txt'
    return open(f_name).read().splitlines()