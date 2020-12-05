from functools import reduce
from pprint import pprint


def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [line.strip() for line in input_file.readlines()]


def determine_row(card):
    return sum([2**(6-i) if c == "B" else 0 for (i, c) in enumerate(card)])


def determin_column(card):
    return sum([2**(2-i) if c == "R" else 0 for (i, c) in enumerate(card)])


def calculate_ids(data):
    return [determine_row(card[:7]) * 8 + determin_column(card[7:]) for card in data]


def solve_first(data):
    return max(calculate_ids(data))


def solve_second(data):
    ids = calculate_ids(data)
    ids.sort()
    return reduce(lambda a, b: b if int(b)-int(a) == 1 else a, ids) + 1


if __name__ == "__main__":
    data = get_input("day5_input.txt")
    result = solve_second(data)
    print(result)
