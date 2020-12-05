import re


def get_input(file_name):
    with open(file_name, "r") as input_file:
        data = []
        card = []
        lines = [line.strip() for line in input_file.readlines()]
        for line in lines:
            if line:
                card.extend([part.split(":") for part in line.split(" ")])
            else:
                data.append(card)
                card = []
        data.append(card)
    return data


def all_fields_are_present(card):
    requried = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    s = set([field[0] for field in card])
    return s >= requried


def all_fields_are_valid(card):
    rules = {"byr": r"(19[2-8][0-9]|199[0-9]|200[0-2])",
             "iyr": r"(201[0-9]|2020)", "eyr": r"(202[0-9]|2030)",
             "hgt": r"((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)",
             "hcl": r"#([0-9]|[a-f]){6}",
             "ecl": r"(amb|blu|brn|gry|grn|hzl|oth)", "pid": r"[0-9]{9}", "cid": ".*"}
    for key, value in card:
        if not re.fullmatch(rules[key], value):
            return False
    return True


def solve_first(data):
    # test for all sets if required is subset of set
    # then add all booleans which result from the tests
    return sum([all_fields_are_present(card) for card in data])


def solve_second(data):
    return sum([all_fields_are_present(card) and all_fields_are_valid(card) for card in data])


if __name__ == "__main__":
    data = get_input("day4_input.txt")
    # pprint(data)
    result = solve_second(data)
    print(result)
