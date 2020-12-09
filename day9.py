def get_data(file_name):
    with open(file_name, "r") as input_file:
        return [int(line.strip()) for line in input_file.readlines()]


def is_sumable(number, preamble):
    for pre in preamble:
        if number - pre in preamble:
            return True
    return False


def solve_first(numbers, preamble_length):
    for number_index, number in enumerate(numbers[preamble_length:]):
        preamble = numbers[number_index:number_index+preamble_length]
        if not is_sumable(number, preamble):
            return number
    return "nothing found"


def solve_second(numbers, preamble_length):
    invalid_number = solve_first(numbers, preamble_length)
    invalid_number_index = numbers.index(invalid_number)
    for window_width in range(2, invalid_number_index):
        for window_start in range(len(numbers[:invalid_number_index-window_width])):
            nums = numbers[window_start:window_start+window_width]
            if sum(nums) == invalid_number:
                return min(nums)+max(nums)

    return "nothing found"


if __name__ == "__main__":
    numbers = get_data("day9_input.txt")
    result = solve_second(numbers, 25)
    print(result)
