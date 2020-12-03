from pprint import pprint


def get_input(file_name):
    with open(file_name, "r") as input_file:
        # re would be prettier
        return [line.strip().replace(":", "").replace("-", " ").split(" ") for line in input_file.readlines()]


def solve_first(passwords):
    amount_correct_passwords = 0
    for minimal_amount, maximal_amount, char, password in passwords:
        occurrences = len([c for c in password if c == char])
        if int(minimal_amount) <= occurrences <= int(maximal_amount):
            amount_correct_passwords += 1
    return amount_correct_passwords


def xor(a, b):
    return (a and not b) or (not a and b)


def solve_second(passwords):
    amount_correct_passwords = 0
    for first_position, second_position, char, password in passwords:
        first_char = password[int(first_position) - 1]
        second_char = password[int(second_position) - 1]
        if xor(char == first_char, char == second_char):
            amount_correct_passwords += 1
    return amount_correct_passwords


if __name__ == "__main__":
    inp = get_input("day2_input.txt")
    amount_correct_passwords = solve_second(inp)
    print(amount_correct_passwords)
