from pprint import pprint
from functools import reduce


def get_input(file_name):
    with open(file_name, "r") as input_file:
        return list([line.strip() for line in input_file.readlines()])


def solve_first(inp, steps_right, steps_down):
    row = column = tree_counter = 0
    last_row = len(inp) - 1
    row_length = len(inp[0])
    while row < last_row:
        row += steps_down
        column = (column+steps_right) % row_length
        tree_counter += 1 if inp[row][column] == "#" else 0
    return tree_counter


def solve_second(inp):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_counters = [solve_first(inp, *slope) for slope in slopes]
    return reduce(lambda x, y: x*y, tree_counters)


if __name__ == "__main__":
    inp = get_input("day3_input.txt")
    tree_counter = solve_second(inp)
    print(tree_counter)
