# Part one
def part1(lines: list):
    data = []
    for line in lines:
        data.append([int(x) for x in line.strip().split()])

    # First build the pyramids
    bdiff = []
    for data_line in data:
        i = 0
        diff = []
        while True:
            ldiff = []
            for num in range(len(data_line)):
                if num == 0:
                    continue
                ldiff.append(data_line[num] - data_line[num - 1])

            diff.append(ldiff)
            data_line = ldiff
            if all(v == 0 for v in ldiff):
                break
        bdiff.append(diff)

    # Reverse the sequence
    total = 0
    for i, line_diff in enumerate(bdiff):
        sub_total = 0
        for diff in line_diff:
            sub_total += diff[-1]  # add last item
        total += sub_total + data[i][-1]  # combine with data

    return total


# Part two
def part2(lines: list):
    data = []
    for line in lines:
        data_list = [int(x) for x in line.strip().split()]
        data_list.reverse()  # Just reverse the list to run backwards in time
        data.append(data_list)

    # Below is the same as part 1
    # First build the pyramids
    bdiff = []
    for data_line in data:
        i = 0
        diff = []
        while True:
            ldiff = []
            for num in range(len(data_line)):
                if num == 0:
                    continue
                ldiff.append(data_line[num] - data_line[num - 1])

            diff.append(ldiff)
            data_line = ldiff
            if all(v == 0 for v in ldiff):
                break
        bdiff.append(diff)

    # Reverse the sequence
    total = 0
    for i, line_diff in enumerate(bdiff):
        sub_total = 0
        for diff in line_diff:
            sub_total += diff[-1]  # add last item
        total += sub_total + data[i][-1]  # combine with data

    return total


if __name__ == "__main__":
    with open("data/day9.txt") as file:
        lines = list(file)
        part1_ans = part1(lines)
        part2_ans = part2(lines)
        print(f"Answer for Part 1: {part1_ans}")
        print(f"Answer for Part 2: {part2_ans}")
