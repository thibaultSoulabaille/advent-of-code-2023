import json
import os.path

import requests
from typing import Any


def get_input(day: int) -> str:
    with open("config/get_input_cookies.json") as cookies_file:
        cookies = json.load(cookies_file)

    req = requests.get(
        url=f"https://adventofcode.com/2023/day/{day}/input",
        cookies=cookies
    )

    if req.status_code == 200:
        return req.text
    return ""


def save_input_file(day: int) -> None:
    output_path = f"input/day_{day}.txt"
    if not os.path.exists(output_path):
        input_content = get_input(day)
        with open(output_path, "w+") as out_file:
            out_file.write(input_content)


def open_input(day: int, test: bool = False, as_list: bool = True) -> Any:
    if test:
        f_name = f'input/test/day_{day}_test.txt'
    else:
        save_input_file(day)
        f_name = f'input/day_{day}.txt'
    if as_list:
        return open(f_name).read().splitlines()
    return open(f_name).read()
