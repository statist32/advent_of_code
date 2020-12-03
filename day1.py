def get_input(file_name):
    with open(file_name, "r") as input_file:
        return list([int(line) for line in input_file.readlines()])


def solve_day1_first(numbers, requested_sum):
    for number in numbers:
        rest = requested_sum-number
        if rest in numbers:
            return number*rest


def solve_day1_second(numbers, requested_sum):
    for i, first in enumerate(numbers):
        for j, second in enumerate(numbers[i:]):
            for third in numbers[i+j:]:
                if (first+second+third == requested_sum):
                    return(first*second*third)


if __name__ == "__main__":
    inp = get_input("day1_input.txt")
    result = solve_day1_second(inp, 2020)
    print(result)
