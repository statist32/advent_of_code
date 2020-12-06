import string
from pprint import pprint


def get_input_first(file_name):
    with open(file_name, "r") as input_file:
        data = []
        group = set()
        lines = [line.strip() for line in input_file.readlines()]
        for line in lines:
            if line:
                for c in line:
                    group.add(c)
            else:
                data.append(group)
                group = set()
        data.append(group)
    return data


def solve_first(data):
    return sum([len(d) for d in data])


def generate_full_set():
    s = set()
    for c in string.ascii_lowercase:
        s.add(c)
    return s


def get_input_second(file_name):
    with open(file_name, "r") as input_file:
        data = []
        group = generate_full_set()
        lines = [line.strip() for line in input_file.readlines()]
        for line in lines:
            if line:
                temp_set = set()
                for c in line:
                    temp_set.add(c)
                group &= temp_set
            else:
                data.append(group)
                group = generate_full_set()
        data.append(group)
    return data


def solve_second(data):
    return sum([len(d) for d in data])


if __name__ == "__main__":
    data = get_input_first("day6_input.txt")
    result = solve_first(data)
    print(result)
    data = get_input_second("day6_input.txt")
    result = solve_second(data)
    print(result)
