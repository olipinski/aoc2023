import re

# Part one
def part1(lines: list):
    total = 0
    conditions = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    for line in lines:
        can_exist = True
        game, info = line.split(":")
        id = game.split(" ")[1]
        info_list = info.split(";")
        info_list = [re.sub(r"\n","",info) for info in info_list] # Remove all new lines
        info_list = [re.sub(",", "", info) for info in info_list] # Remove all commas
        info_list = [info.strip() for info in info_list]  # Remove all leading and trailing whitespaces
        for info in info_list:
            info_split = info.split()
            info_ints = info_split[::2]
            info_words = info_split[1::2]
            info_dict = dict(zip(info_words, info_ints))
            for key in info_dict.keys():
                if int(info_dict[key]) > conditions[key]:
                    can_exist = False
        if can_exist:
          total += int(id)
    return total


# Part two
# Include also spelled out digits
def part2(lines: list):
    total = 0
    for line in lines:
        min_set = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        res = 1
        _, info = line.split(":")
        info_list = info.split(";")
        info_list = [re.sub(r"\n", "", info) for info in info_list]  # Remove all new lines
        info_list = [re.sub(",", "", info) for info in info_list]  # Remove all commas
        info_list = [info.strip() for info in info_list]  # Remove all leading and trailing whitespaces
        for info in info_list:
            info_split = info.split()
            info_ints = info_split[::2]
            info_words = info_split[1::2]
            info_dict = dict(zip(info_words, info_ints))
            for key in info_dict.keys():
                if int(info_dict[key]) > min_set[key]:
                    min_set[key] = int(info_dict[key])
        for val in min_set.values():
            res *= val
        total += res

    return total

if __name__ == "__main__":
    with open("data/day2.txt") as file:
        lines = list(file)
        part1_ans = part1(lines)
        part2_ans = part2(lines)
        print(f"Answer for Part 1: {part1_ans}")
        print(f"Answer for Part 2: {part2_ans}")
