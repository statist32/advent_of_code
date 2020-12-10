def get_data(file_name):
    with open(file_name, "r") as input_file:
        return [int(line.strip()) for line in input_file.readlines()]


def solve_first(numbers):
    differences = {0: 0, 1: 0, 2: 0, 3: 0}
    i = 0
    while i < len(numbers)-1:
        differences[numbers[i+1]-numbers[i]] += 1
        i += 1
    return differences, differences[1] * differences[3]


def solve_second(numbers):
    table_dict = {0: 1, 1: 1}
    for num in numbers[2:]:
        possible_keys = [p_key for p_key in range(
            num-3, num) if p_key in table_dict]
        table_dict[num] = sum([table_dict[x] for x in possible_keys])
    return table_dict


if __name__ == "__main__":
    data = sorted(get_data("day10_input.txt"))
    CHARGING_OUTLET = 0
    DEVICE = max(data)+3
    numbers = [CHARGING_OUTLET, *data, DEVICE]
    result = solve_second(numbers)
    print(result[DEVICE])
