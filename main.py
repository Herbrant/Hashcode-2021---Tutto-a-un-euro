import random 

from Intersection import Intersection
from Schedule import Command, Schedule
from Car import Car
from Street import Street
from State import State
import sys

def main():
    state, intersections, streets, cars = read_input(open(f"input/{sys.argv[1]}.txt", "r"))

    schedules = solve(state, intersections, streets, cars)
    output_lines = __build_output(schedules)

    output(f"output/out_{sys.argv[1]}.txt", output_lines)

def __build_output(schedules):
    lines = []
    lines.append(str(len(schedules)))

    for schedule in schedules:
        lines.append(str(schedule.i))
        lines.append(str(schedule.E))
        for command in schedule.commands:
            lines.append(f"{command.name} {command.T}")

    return lines

def output(filename, lines):
    outfile = open(filename, "w")

    outfile.write("\n".join(lines))

def solve(state, intersections, streets, cars):
    # print(state)

    # print("\nStreets")
    # for _, street in streets.items():
    #     print("#####")
    #     print(street)

    # print("\nCars")
    # for car in cars:
    #     print(car)

    # print ("\nIntersections")
    # for intersection in intersections:
    #     print(intersection)

    schedules = []

    naive_counts = 0

    for intersection in intersections:
        priorities = dict()

        total_interested_cars = 0
        for street in intersection.streets:
            total_interested_cars += street.interested_cars

        # loop_size = max(1, total_interested_cars)
        base_time = 2

        schedule = Schedule()
        schedule.i = intersection.id

        if total_interested_cars > 0:
            for street in intersection.streets:
                priorities[street.name] = street.interested_cars / total_interested_cars

            for street in intersection.streets:
                time_span = base_time # int(loop_size * priorities[street.name])
                schedule.add_command(Command(street.name, time_span))

        # Naive, when no commands where added activate randomly
        if len(schedule.commands) == 0:
            naive_counts += 1
            for street in intersection.streets:
                schedule.add_command(Command(street.name, base_time))

        schedules.append(schedule)

    print(f"Naive counts: {naive_counts}")

    return schedules

def read_input(input_file):
    lines = input_file.readlines()

    state = __build_state(lines[0])

    intersections = __build_intersections(state)

    streets = __build_streets(lines[1:1 + state.S], intersections)

    cars = __build_cars(lines[1 + state.S: 1 + state.S + state.V], streets)

    return state, intersections, streets, cars

def __build_intersections(state):
    intersections = []

    for i in range(0, state.I):
        inter = Intersection()
        inter.id = i

        intersections.append(inter)
    
    return intersections

def __build_cars(lines, streets):
    cars = []

    for line in lines:
        fragments = line.split(' ')

        car = Car()

        car.P = int(fragments[0])
        for street in fragments[1:]:
            street = street.strip()
            car.add_target(street)
            streets[street].interested_cars += 1

        car.id = len(cars)
        cars.append(car)

        streets[fragments[1]].add_car(car)

    return cars

def __build_streets(lines, intersections):
    streets = dict()

    for line in lines:
        fragments = line.split(' ')
        street = Street()

        street.B = int(fragments[0])
        street.E = int(fragments[1])
        street.name = str(fragments[2]).strip()
        street.L = int(fragments[3])

        streets[street.name] = street

        # intersections[street.B].add_street(street)
        intersections[street.E].add_street(street)

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