import os
import time
from collections import defaultdict

import numpy as np
from joblib import Parallel


# Part one
def part1(lines: list):
    lowest = np.inf
    seeds = None
    maps = defaultdict(list)
    map_id = -1
    for line in lines:
        if "seeds:" in line:
            seeds = line.split(":")[1].strip().split()
            seeds = np.array(seeds).astype(
                np.int64
            )  # Seeds are very large numbers turns out
            continue
        if "map" in line:
            map_id += 1  # We start at 0, because initial value is -1
            continue
        if len(line) > 1:  # Ignore empty lines
            values = np.array(line.split()).astype(np.int64)
            maps[map_id].append(values)

    for seed in seeds:
        for mapx in range(len(maps.keys())):
            for tup in maps[mapx]:
                if tup[1] <= seed < tup[1] + tup[2]:
                    seed = (
                        seed + tup[0] - tup[1]
                    )  # Override the meaning of seed here slightly
                    break
        if seed < lowest:
            lowest = seed
    return lowest


# Part two
def part2(lines: list):
    seed_rv = None
    seed_ranges = []
    maps = defaultdict(list)
    map_id = -1
    for line in lines:
        if "seeds:" in line:
            seed_rv = line.split(":")[1].strip().split()
            seed_rv = np.array(seed_rv).astype(
                np.int64
            )  # Seeds are very large numbers turns out
            continue
        if "map" in line:
            map_id += 1  # We start at 0, because initial value is -1
            continue
        if len(line) > 1:  # Ignore empty lines
            values = np.array(line.split()).astype(np.int64)
            maps[map_id].append(values)

    for seed_no in range(0, len(seed_rv), 2):
        seed_ranges.append((seed_rv[seed_no], seed_rv[seed_no] + seed_rv[seed_no + 1]))

    # There's a smart way to do this
    # By computing each range boundary and passing it through the mappings
    # But it makes my brain hurt
    # So bruteforce it is

    seed_ranges = [range(seed[0], seed[1]) for seed in seed_ranges]

    def compute_lowest_seed(seed_range):
        lowest = np.inf
        for seed in seed_range:
            for mapx in range(len(maps.keys())):
                for tup in maps[mapx]:
                    if tup[1] <= seed < tup[1] + tup[2]:
                        seed = (
                            seed + tup[0] - tup[1]
                        )  # Override the meaning of seed here slightly
                        break
            if seed < lowest:
                lowest = seed
        return lowest

    start_time = time.perf_counter()

    results = Parallel(n_jobs=os.cpu_count(), verbose=10)(
        (compute_lowest_seed, (range,), {}) for range in seed_ranges
    )

    finish_time = time.perf_counter()

    print(f"Computing lowest value finished in {finish_time - start_time} seconds")

    print(results)

    return min(results)


if __name__ == "__main__":
    with open("data/day5.txt") as file:
        lines = list(file)
        part1_ans = part1(lines)
        part2_ans = part2(lines)
        print(f"Answer for Part 1: {part1_ans}")
        print(f"Answer for Part 2: {part2_ans}")
