from pprint import pprint
from copy import deepcopy

OCCUPIED_SEAT = "#"
EMPTY_SEAT = "L"
FLOOR = "."


def get_data(file_name):
    with open(file_name, "r") as input_file:
        return [[c for c in line.strip()] for line in input_file.readlines()]


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))
    print("")


def add_tuple(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1])


def get_adjacent_seats(row, column, max_row, max_column):
    adjacent_offset = [(-1, -1), (-1, 0), (-1, 1),
                       (0, -1),           (0, 1),
                       (1, -1),  (1, 0),  (1, 1)]
    adjacent_seats = []
    for adja in adjacent_offset:
        next_row, next_column = add_tuple(adja, (row, column))
        if -1 < next_row < max_row and -1 < next_column < max_column:
            adjacent_seats.append((next_row, next_column))
    return adjacent_seats


def count_occupied_seats(row, column, seats):
    counter = 0
    max_row = len(seats)
    max_column = len(seats[0])
    adjacent_seats = get_adjacent_seats(row, column, max_row, max_column)
    for seat in adjacent_seats:
        row, column = seat
        if seats[row][column] == OCCUPIED_SEAT:
            counter += 1
    return counter


def count_all_occupied_seats(seats):
    return matrix_to_string(seats).count(OCCUPIED_SEAT)


def iterate_once(seats):
    new_seats = deepcopy(seats)
    for row_index, row in enumerate(seats):
        for column_index, seat in enumerate(row):
            if seats[row_index][column_index] == FLOOR:
                continue
            counter = count_occupied_seats(row_index, column_index, seats)
            if seat == EMPTY_SEAT and counter == 0:
                new_seats[row_index][column_index] = OCCUPIED_SEAT
            elif seat == OCCUPIED_SEAT and counter >= 4:
                new_seats[row_index][column_index] = EMPTY_SEAT
    return new_seats


def matrix_to_string(matrix):
    return "".join(["".join(row) for row in matrix])


def solve_first(seats):
    old_seats = seats
    new_seats = iterate_once(old_seats)
    while matrix_to_string(new_seats) != matrix_to_string(old_seats):
        old_seats = new_seats
        new_seats = iterate_once(old_seats)
    return count_all_occupied_seats(new_seats)


if __name__ == "__main__":
    seats = get_data("day11_input.txt")
    result = solve_first(seats)
    print(result)
