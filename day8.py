from copy import deepcopy


def get_data(file_name):
    with open(file_name, "r") as input_file:
        return [line.strip() for line in input_file.readlines()]


def parse_data(data):
    return [[line_number, *[part if part.isalpha() else int(part) for part in line_content.split()]] for line_number, line_content in enumerate(data)]


def solve_first(code):
    # returns (Bool, acc) False if infinit loop
    acc = 0
    line_numbers = []
    line_number, instruction, instruction_value = code[0]
    last_line = len(code) - 1
    while line_number not in line_numbers:
        line_numbers.append(line_number)
        if line_number == last_line:
            # program terminated corretly
            return (True, acc + (instruction_value if instruction == "acc" else 0))
        nx_line_number, nx_instruction, nx_instruction_value = code[line_number+1]
        if instruction == "acc":
            acc += instruction_value
        elif instruction == "jmp":
            nx_line_number, nx_instruction, nx_instruction_value = code[
                line_number+instruction_value]

        line_number, instruction, instruction_value = nx_line_number, nx_instruction, nx_instruction_value
    return (False, acc)


def solve_second(code):
    for line_number, instruction, _ in code:
        new_code = deepcopy(code)
        result = [False]
        if instruction == "nop":
            new_code[line_number][1] = "jmp"
            result = solve_first(new_code)
        elif instruction == "jmp":
            new_code[line_number][1] = "nop"
            result = solve_first(new_code)
        if result[0]:
            return result


if __name__ == "__main__":
    data = get_data("day8_input.txt")
    code = parse_data(data)
    result = solve_second(code)
    print(result)
