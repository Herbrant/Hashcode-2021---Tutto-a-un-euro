import os, sys

def main():
    read_input(open(f"input/{sys.argv[1]}.txt", "r"))

    output_lines = solve()
    output(f"output/out_{sys.argv[1]}.txt", output_lines)

def output(filename, lines):
    outfile = open(filename, "w")

    outfile.writelines(lines)

def solve():
    return []

def read_input(input_file):
    lines = input_file.readlines()

    for line in lines:
        print(line.strip())

if __name__ == "__main__":
    main()