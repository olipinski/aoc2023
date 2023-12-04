import numpy as np


def part1(lines: list):
    total = 0
    for line in lines:
        winning_numbers = line.split(":")[1].split("|")[0].strip().split()
        winning_numbers = np.array(winning_numbers).astype(np.int32)
        my_numbers = line.split(":")[1].split("|")[1].strip().split()
        my_numbers = np.array(my_numbers).astype(np.int32)
        no_win_numbers = np.intersect1d(winning_numbers, my_numbers).shape[0]
        if no_win_numbers > 0:
            total += 2 ** (no_win_numbers - 1)
    return total


def part2(lines: list):
    # Add initial cards
    line_multiplier = np.ones(len(lines), dtype=np.int32)
    for line in lines:
        line_id = int(line.split(":")[0].split("d")[1].strip())
        winning_numbers = line.split(":")[1].split("|")[0].strip().split()
        winning_numbers = np.array(winning_numbers).astype(np.int32)
        my_numbers = line.split(":")[1].split("|")[1].strip().split()
        my_numbers = np.array(my_numbers).astype(np.int32)
        no_win_numbers = np.intersect1d(winning_numbers, my_numbers).shape[0]
        line_multiplier[line_id: line_id + no_win_numbers] += 1 * line_multiplier[line_id-1]

    total = np.sum(line_multiplier)
    return total


if __name__ == "__main__":
    with open("data/day4.txt") as file:
        lines = list(file)
        part1_ans = part1(lines)
        part2_ans = part2(lines)
        print(f"Answer for Part 1: {part1_ans}")
        print(f"Answer for Part 2: {part2_ans}")
