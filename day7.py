from pprint import pprint


def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [line.strip() for line in input_file.readlines()]


def parse_data(data):
    parsed_data = {}
    for rule in data:
        r = rule.replace(".", "").replace(
            ",", "").replace("s contain", "").split("bag")
        parsed_data[r[0].strip()] = [inner_bag.strip()[2:].split(" ", 1) if inner_bag.strip().startswith("s") else inner_bag.strip().split(" ", 1)
                                     for inner_bag in r[1:-1]]
    return parsed_data


def recursion1(rules, color):
    if color == "other":
        return False
    if color == "shiny gold":
        return True
    contained_bags = rules[color]
    return bool(sum([recursion1(rules, bag[1]) for bag in contained_bags]))


def solve_first(rules):
    colors = rules.keys()
    return sum([bool(recursion1(rules, color))
                for color in colors if color != "shiny gold"])


def recursion2(rules, color):
    contained_bags = rules[color]
    contained_bags_amount = sum(
        [int(r[0]) if r[0] != "no" else 0 for r in rules[color]])
    s = [recursion2(rules, bag[1]) * int(bag[0]) if bag[0] != "no" else 0
         for bag in contained_bags]
    return sum(s) + contained_bags_amount


def solve_second(rules):
    color = "shiny gold"
    s = [recursion2(rules, color)]
    return sum(s)


if __name__ == "__main__":
    data = get_input("day7_input.txt")
    rules = parse_data(data)
    result = solve_second(rules)
    pprint(result)
