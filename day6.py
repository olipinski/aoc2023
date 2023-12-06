import math


# Part one
def part1(lines: list):
    total_wins = []
    times = []
    distances = []
    for line in lines:
        if "Time" in line:
            times = [int(time) for time in line.split(":")[1].strip().split()]
        else:  # Distance
            distances = [
                int(distance) for distance in line.split(":")[1].strip().split()
            ]

    for time, distance in zip(times, distances):
        wins = 0
        for t in range(1, time):
            # calculate distance
            dist_travelled = t * (time - t)
            if dist_travelled > distance:
                wins += 1
        total_wins.append(wins)

    return math.prod(total_wins)


# Part two
def part2(lines: list):
    total_wins = []
    time = 0
    distance = 0
    for line in lines:
        if "Time" in line:
            time = int(line.split(":")[1].strip().replace(" ", ""))
        else:  # Distance
            distance = int(line.split(":")[1].strip().replace(" ", ""))

    wins = 0
    for t in range(1, time):
        # calculate distance
        dist_travelled = t * (time - t)
        if dist_travelled > distance:
            wins += 1
    total_wins.append(wins)

    return math.prod(total_wins)


if __name__ == "__main__":
    with open("data/day6.txt") as file:
        lines = list(file)
        part1_ans = part1(lines)
        part2_ans = part2(lines)
        print(f"Answer for Part 1: {part1_ans}")
        print(f"Answer for Part 2: {part2_ans}")
