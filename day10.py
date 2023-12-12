import copy


# Part one
def part1(lines: list):
    # Valid pipes and the way they connect on the x,y axes
    # spelled out so it's easier to read
    # (0,0) is top left corner
    # y/x - - >
    # |
    # |
    pipes = {
        "|": {
            "x": [],
            "y": [-1, 1],
        },
        "-": {
            "x": [-1, 1],
            "y": [],
        },
        "L": {
            "x": [1],
            "y": [-1],
        },
        "J": {
            "x": [-1],
            "y": [-1],
        },
        "7": {
            "x": [-1],
            "y": [1],
        },
        "F": {
            "x": [1],
            "y": [1],
        },
        ".": {
            "x": [],
            "y": [],
        },
        # For our input s is a -
        "S": {"x": [-1, 1], "y": []},  # [-1, 1],
    }
    start = None
    boundaries = None
    for y, line in enumerate(lines):
        if "S" in line:
            x = line.index("S")
            start = (x, y)
            # Set boundaries here for ease of access
            boundaries = (len(line), len(lines))
            break

    # On a 2-d grid there will always be an even number of pipes
    # So our steps can just be halved after we go back to S

    steps = 0
    points_to_visit = [start]
    finished = False
    visited = []
    while not finished:
        new_points = []
        for point in points_to_visit:
            char = lines[point[1]][point[0]]

            for valid_x in pipes[char]["x"]:
                next_dir_x = valid_x + point[0]
                if (
                    0 <= next_dir_x < boundaries[0]
                    and (next_dir_x, point[1]) not in visited
                ):
                    new_points.append((next_dir_x, point[1]))

            for valid_y in pipes[char]["y"]:
                next_dir_y = valid_y + point[1]
                if (
                    0 <= next_dir_y < boundaries[1]
                    and (point[0], next_dir_y) not in visited
                ):
                    new_points.append((point[0], next_dir_y))

            visited.append(point)

        if len(points_to_visit) == 0:
            finished = True
            break

        steps += 1
        points_to_visit = copy.deepcopy(new_points)
        # print(f"{visited=}")
        # print(f"{points_to_visit=}")

    return steps - 1


# Part two
def part2(lines: list):
    # Valid pipes and the way they connect on the x,y axes
    # spelled out so it's easier to read
    # (0,0) is top left corner
    # y/x - - >
    # |
    # |
    pipes = {
        "|": {
            "x": [],
            "y": [-1, 1],
        },
        "-": {
            "x": [-1, 1],
            "y": [],
        },
        "L": {
            "x": [1],
            "y": [-1],
        },
        "J": {
            "x": [-1],
            "y": [-1],
        },
        "7": {
            "x": [-1],
            "y": [1],
        },
        "F": {
            "x": [1],
            "y": [1],
        },
        ".": {
            "x": [],
            "y": [],
        },
        # For our input s is a -
        "S": {"x": [-1, 1], "y": []},  # [-1, 1],
    }
    start = None
    boundaries = None
    for y, line in enumerate(lines):
        if "S" in line:
            x = line.index("S")
            start = (x, y)
            # Set boundaries here for ease of access
            boundaries = (len(line), len(lines))
            break

    # On a 2-d grid there will always be an even number of pipes
    # So our steps can just be halved after we go back to S

    steps = 0
    points_to_visit = [start]
    finished = False
    visited = []
    while not finished:
        new_points = []
        for point in points_to_visit:
            char = lines[point[1]][point[0]]

            for valid_x in pipes[char]["x"]:
                next_dir_x = valid_x + point[0]
                if (
                    0 <= next_dir_x < boundaries[0]
                    and (next_dir_x, point[1]) not in visited
                ):
                    new_points.append((next_dir_x, point[1]))

            for valid_y in pipes[char]["y"]:
                next_dir_y = valid_y + point[1]
                if (
                    0 <= next_dir_y < boundaries[1]
                    and (point[0], next_dir_y) not in visited
                ):
                    new_points.append((point[0], next_dir_y))

            visited.append(point)

        if len(points_to_visit) == 0:
            finished = True
            break

        steps += 1
        points_to_visit = copy.deepcopy(new_points)

    # Remove all unnecessary points
    for y in range(boundaries[1]):
        for x in range(boundaries[0]):
            if (x, y) not in visited:
                lines[y] = list(lines[y])
                lines[y][x] = "."
                lines[y] = "".join(lines[y])

    # Print a nice cleaned up map
    # for line in lines:
    #     print(line)

    # Count crossings
    count = 0
    for y in range(boundaries[1]):
        crossings = 0
        chars = list(lines[y])
        x = 0
        while x < boundaries[0]:
            char_comb = ""
            z = x
            if chars[x] in ["F", "L"]:
                while z < boundaries[0]:
                    if chars[z] not in ["F", "L", "-"]:
                        break
                    z += 1
                char_comb = char_comb.join([chars[x], chars[z]])
            if char_comb in ["FJ", "L7"]:
                crossings += 1
                x = z + 1
                continue
            elif chars[x] in [
                "F",
                "7",
                "|",
                "J",
                "L",
                "S",
            ]:  # these are one crossing each
                crossings += 1
            elif chars[x] in ["S", "-"]:  # for us S is a -
                pass
            else:
                if crossings % 2 == 1:
                    count += 1
            x += 1

    return count


if __name__ == "__main__":
    with open("data/day10.txt") as file:
        lines = list(file)
        part1_ans = part1(lines)
        part2_ans = part2(lines)
        print(f"Answer for Part 1: {part1_ans}")
        print(f"Answer for Part 2: {part2_ans}")
