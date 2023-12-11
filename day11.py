import copy

import numpy as np
import scipy


# Part one
def part1(lines: list):
    expanded_rows = []
    for line in lines:
        line = line.replace("#", "1")
        line = line.replace(".", "0")
        line = line.strip()
        expanded_rows.append([int(x) for x in [*line]])
        if "1" not in line:
            expanded_rows.append([int(x) for x in [*line]])

    expanded_rows = np.array(expanded_rows)
    expanded_rows_copy = copy.deepcopy(expanded_rows)

    inserted = 0
    for column in range(expanded_rows_copy.shape[1]):
        if 1 not in expanded_rows_copy[:, column]:
            expanded_rows = np.insert(expanded_rows, column + inserted, 0, axis=1)
            inserted += 1

    del expanded_rows_copy

    x, y = np.where(expanded_rows == 1)

    coords = list(zip(x, y))

    distances = scipy.spatial.distance.pdist(coords, "cityblock")

    return int(sum(distances))


# Part two
def part2(lines: list):
    data = []
    for line in lines:
        line = line.replace("#", "1")
        line = line.replace(".", "0")
        line = line.strip()
        data.append([int(x) for x in [*line]])

    data = np.array(data)

    exp_columns = []
    exp_rows = []

    for column in range(data.shape[1]):
        if 1 not in data[:, column]:
            exp_columns.append(column)

    for row in range(data.shape[0]):
        if 1 not in data[row, :]:
            exp_rows.append(row)

    exp_columns = np.array(exp_columns)
    exp_rows = np.array(exp_rows)

    x, y = np.where(data == 1)

    coords = list(zip(x, y))

    new_coords = []
    for coord in coords:
        expanded_rows = np.where(exp_rows < coord[0])
        expanded_columns = np.where(exp_columns < coord[1])
        adx = expanded_rows[0].shape[0]
        ady = expanded_columns[0].shape[0]
        new_x = coord[0] + (adx * 999999)
        new_y = coord[1] + (ady * 999999)
        new_coords.append((new_x, new_y))

    distances = scipy.spatial.distance.pdist(new_coords, "cityblock")

    return int(sum(distances))


if __name__ == "__main__":
    with open("data/day11.txt") as file:
        lines = list(file)
        part1_ans = part1(lines)
        part2_ans = part2(lines)
        print(f"Answer for Part 1: {part1_ans}")
        print(f"Answer for Part 2: {part2_ans}")
