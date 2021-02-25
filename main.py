from Car import Car
from Street import Street
from State import State
import sys

def main():
    state, streets, cars = read_input(open(f"input/{sys.argv[1]}.txt", "r"))

    output_lines = solve(state, streets, cars)

    output(f"output/out_{sys.argv[1]}.txt", output_lines)

def output(filename, lines):
    outfile = open(filename, "w")

    outfile.writelines(lines)

def solve(state, streets, cars):
    print(state)

    print("Streets")
    for street in streets:
        print("#####")
        print(street)

    print("Cars")
    for car in cars:
        print("#####")
        print(car)

    return []

def read_input(input_file):
    lines = input_file.readlines()

    state = __build_state(lines[0])

    streets = __build_streets(lines[1:1 + state.S])

    cars = __build_cars(lines[1 + state.S: 1 + state.S + state.V])

    return state, streets, cars

def __build_cars(lines):
    cars = []

    for line in lines:
        fragments = line.split(' ')

        car = Car()

        car.P = int(fragments[0])
        for street in fragments[1:]:
            car.add_target(street.strip())

        cars.append(car)

    return cars

def __build_streets(lines):
    streets = []

    for line in lines:
        fragments = line.split(' ')
        street = Street()

        street.B = int(fragments[0])
        street.E = int(fragments[1])
        street.name = str(fragments[2]).strip()
        street.L = int(fragments[3])

        streets.append(street)

    return streets

def __build_state(line: str):
    state = State()

    fragments = line.split(' ')

    state.D = int(fragments[0])
    state.I = int(fragments[1])
    state.S = int(fragments[2])
    state.V = int(fragments[3])
    state.F = int(fragments[4])

    return state

if __name__ == "__main__":
    main()