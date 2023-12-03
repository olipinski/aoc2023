import re


# Part one
# Only include digits which are numbers
def part1(lines: list):
    total = 0
    for line in lines:
        integers = re.findall(r"\d", line)
        number = int("".join([integers[0], integers[-1]]))
        total += number
    print(total)


# Part two
# Include also spelled out digits
def part2(lines: list):
    search_list = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        r"\d",
    ]
    int_map = dict(
        zip(search_list, [i for i in range(1, 10)])
    )  # This skips the \d at the end
    total = 0
    for line in lines:
        integers = re.findall(r"(?=(" + "|".join(search_list) + r"))", line)
        for idx, integer in enumerate(integers):
            if integer in int_map.keys():
                integers[idx] = int_map[integer]
        number = int("".join([str(integers[0]), str(integers[-1])]))
        total += number
    print(total)


if __name__ == "__main__":
    with open("data/day1.txt") as file:
        lines = list(file)
        part1_ans = part1(lines)
        part2_ans = part2(lines)
        print(f"Answer for Part 1: {part1_ans}")
        print(f"Answer for Part 2: {part2_ans}")
