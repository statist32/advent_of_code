def get_data(file_name):
    with open(file_name, "r") as input_file:
        return [[int(num) if num != "x" else "x" for num in line.strip().split(",")] for line in input_file.readlines()]


def solve_first(data):
    time = data[0][0]
    ids = [d for d in data[1] if d != "x"]
    detature_times = [(id, (time//id + 1)*id) for id in ids]
    first_bus = min(detature_times, key=lambda time: time[1])
    return first_bus[0] * (first_bus[1] - time)


def calculate_occurence(n1, n2, offset1,  required_diff):
    # find first point when the pattern occures
    # every offset+ n1*n2 point the pattern will be there again
    a1 = 1
    diff = (a1 * n1) % n2
    while diff != (required_diff % n2):
        a1 += 1
        diff = (a1 * n1 + offset1) % (n2)
    return a1*n1 + offset1,  n1*n2


def solve_second(ids):
    # get find pattern of the first two numbers, first two and third, first three and fourth ...
    numbers = [(i, id)for i, id in enumerate(ids) if id != "x"]
    base_number = numbers[0][1]
    offset = 0
    for i, number in numbers[1:]:
        offset, base_number = calculate_occurence(
            base_number, number, offset, -i)
    return offset


if __name__ == "__main__":
    data = get_data("day13_input.txt")
    result = solve_second(data[1])
    print(result)
