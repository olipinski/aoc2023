import math


# Part one
def part1(lines: list):
    line_0 = True
    nodes_cons = {}
    directions = []
    for line in lines:
        if line_0:
            directions = [*line.strip()]
            temp_list = []
            for direction in directions:
                if direction == "R":
                    temp_list.append(1)
                elif direction == "L":
                    temp_list.append(0)
                else:
                    print("Invalid directions.")
            directions = temp_list
        elif line.strip() != "":
            root = line.split("=")[0].strip()
            nodes = line.split("=")[1].strip().strip("(").strip(")").split(",")
            nodes_cons[root] = (nodes[0].strip(), nodes[1].strip())
        line_0 = False

    start_node = "AAA"
    steps = 0
    loop = True
    while loop:
        for direction in directions:
            if start_node == "ZZZ":
                loop = False
                break
            start_node = nodes_cons[start_node][direction]
            steps += 1

    return steps


# Part two
def part2(lines: list):
    line_0 = True
    nodes_cons = {}
    directions = []
    for line in lines:
        if line_0:
            directions = [*line.strip()]
            temp_list = []
            for direction in directions:
                if direction == "R":
                    temp_list.append(1)
                elif direction == "L":
                    temp_list.append(0)
                else:
                    print("Invalid directions.")
            directions = temp_list
        elif line.strip() != "":
            root = line.split("=")[0].strip()
            nodes = line.split("=")[1].strip().strip("(").strip(")").split(",")
            nodes_cons[root] = (nodes[0].strip(), nodes[1].strip())
        line_0 = False

    start_nodes = []
    for root in nodes_cons.keys():
        if "A" == [*root][2]:
            start_nodes.append(root)

    # General solutions
    # It's very slow
    # steps = 0
    # loop = True
    # while loop:
    #     for direction in directions:
    #         all = True
    #         new_nodes = []
    #         for start_node in start_nodes:
    #             new_node = nodes_cons[start_node][direction]
    #             new_nodes.append(new_node)
    #         steps += 1
    #
    #         for node in new_nodes:
    #             if not "Z" == [*node][2]:
    #                 all = False
    #
    #         start_nodes = new_nodes
    #
    #         if all:
    #             loop = False
    #             break

    # Input solution
    # Using LCM
    steps_list = []
    for start_node in start_nodes:
        steps = 0
        loop = True
        while loop:
            for direction in directions:
                if [*start_node][2] == "Z":
                    steps_list.append(steps)
                    loop = False
                    break
                start_node = nodes_cons[start_node][direction]
                steps += 1
    steps = math.lcm(*steps_list)

    return steps


if __name__ == "__main__":
    with open("data/day8.txt") as file:
        lines = list(file)
        part1_ans = part1(lines)
        part2_ans = part2(lines)
        print(f"Answer for Part 1: {part1_ans}")
        print(f"Answer for Part 2: {part2_ans}")
