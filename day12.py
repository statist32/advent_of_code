STARTING_DIRECTION = "E"
DIRECTIONS = ["N", "E", "S", "W"]
DIRECTION_AMOUNT = len(DIRECTIONS)


class Ship1():
    def __init__(self):
        self.direction = STARTING_DIRECTION
        self.north = 0
        self.east = 0

    def manhattan_distance(self):
        return abs(self.north) + abs(self.east)

    def rotate(self, direction, degrees):
        steps = degrees % 360 // 90
        if direction == "L":
            steps = DIRECTION_AMOUNT - steps
        current_index = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(current_index + steps) % DIRECTION_AMOUNT]

    def move(self, direction, units):
        if direction == "N":
            self.north += units
        elif direction == "S":
            self.north -= units
        elif direction == "E":
            self.east += units
        elif direction == "W":
            self.east -= units
        elif direction == "F":
            self.move(self.direction, units)


class Ship2():
    def __init__(self):
        self.way_north = 1
        self.way_east = 10
        self.north = 0
        self.east = 0

    def manhattan_distance(self):
        return abs(self.north) + abs(self.east)

    def rotate(self, direction, degrees):
        steps = degrees % 360 // 90
        if direction == "L":
            steps = DIRECTION_AMOUNT - steps
        if steps == 1:
            self.way_north, self.way_east = -self.way_east, self.way_north
        if steps == 2:
            self.way_north, self.way_east = -self.way_north, -self.way_east
        if steps == 3:
            self.way_north, self.way_east = self.way_east, -self.way_north

    def move(self, direction, units):
        if direction == "N":
            self.way_north += units
        elif direction == "S":
            self.way_north -= units
        elif direction == "E":
            self.way_east += units
        elif direction == "W":
            self.way_east -= units

    def forward(self, units):
        self.north += self.way_north*units
        self.east += self.way_east*units


def get_data(file_name):
    with open(file_name, "r") as input_file:
        return [(line.strip()[0], int(line.strip()[1:]))for line in input_file.readlines()]


def solve_first(instructions):
    ship = Ship1()
    for direction, units in instructions:
        if direction in ["F", *DIRECTIONS]:
            ship.move(direction, units)
        else:
            ship.rotate(direction, units)

    distance = ship.manhattan_distance()
    return distance


def solve_second(instructions):
    ship = Ship2()
    for direction, units in instructions:
        if direction == "F":
            ship.forward(units)
        elif direction in DIRECTIONS:
            ship.move(direction, units)
        else:
            ship.rotate(direction, units)
    distance = ship.manhattan_distance()
    return distance


if __name__ == "__main__":
    instructions = get_data("day12_input.txt")
    result = solve_second(instructions)
    print(result)
