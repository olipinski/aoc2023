from collections import defaultdict

import numpy as np


# Part one
# noinspection PyTypedDict,PyTypeChecker
def part1(lines: list):
    facecard_mapping = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
    }
    hand_dict = defaultdict(
        lambda: {
            "hand": None,
            "bid": None,
            "type": -1,
            "type_rank": -1,
            "total_rank": -1,
        }
    )
    for line in lines:
        bid = int(line.split(" ")[1].strip())
        hand = [*line.split(" ")[0].strip()]
        # The actual names of cards don't matter, just their relative ranks
        hand = tuple(
            [
                facecard_mapping[card] if card in facecard_mapping.keys() else int(card)
                for card in hand
            ]
        )
        hand_dict[line.split(" ")[0].strip()]["hand"] = hand
        hand_dict[line.split(" ")[0].strip()]["bid"] = bid

    # First sorting pass
    for key in hand_dict.keys():
        _, counts = np.unique(hand_dict[key]["hand"], return_counts=True)
        if 5 in counts:  # five of a kind
            hand_dict[key]["type"] = 1
        elif 4 in counts:  # four of a kind
            hand_dict[key]["type"] = 2
        elif 3 in counts and 2 in counts:  # full house
            hand_dict[key]["type"] = 3
        elif 3 in counts:  # three of a kind
            hand_dict[key]["type"] = 4
        elif np.count_nonzero(counts == 2) == 2:  # two pair
            hand_dict[key]["type"] = 5
        elif 2 in counts:  # pair
            hand_dict[key]["type"] = 6
        else:  # high card
            hand_dict[key]["type"] = 7

    # Second sorting
    prev_index = 0
    for typei in range(1, 8):
        type_hands = []
        keys = []
        for key in hand_dict.keys():
            if hand_dict[key]["type"] == typei:
                type_hands.append(hand_dict[key]["hand"])
                keys.append(key)

        indices = sorted(
            range(len(type_hands)), key=lambda k: type_hands[k], reverse=True
        )

        for rank, i in enumerate(indices):
            hand_dict[keys[i]]["type_rank"] = prev_index + rank
            hand_dict[keys[i]]["total_rank"] = (
                hand_dict[keys[i]]["type"] * len(hand_dict)
                + hand_dict[keys[i]]["type_rank"]
            )

        prev_index += len(indices)

    to_sort = [
        (
            hand_dict[key]["total_rank"],
            hand_dict[key]["bid"],
        )  # , key, hand_dict[key]["hand"], hand_dict[key]["type"])
        for key in hand_dict.keys()
    ]

    # Sort in reverse, as for us lowest value is best
    to_sort = sorted(to_sort, key=lambda k: k[0], reverse=True)

    total = 0
    for i, val in enumerate(to_sort):
        total += val[1] * (i + 1)  #

    return total


# Part two
def part2(lines: list):
    facecard_mapping = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 1,  # it is now a joker, so lowest value of 1
        "T": 10,
    }
    hand_dict = defaultdict(
        lambda: {
            "hand": None,
            "bid": None,
            "type": -1,
            "type_rank": -1,
            "total_rank": -1,
        }
    )
    for line in lines:
        bid = int(line.split(" ")[1].strip())
        hand = [*line.split(" ")[0].strip()]
        # The actual names of cards don't matter, just their relative ranks
        hand = tuple(
            [
                facecard_mapping[card] if card in facecard_mapping.keys() else int(card)
                for card in hand
            ]
        )
        hand_dict[line.split(" ")[0].strip()]["hand"] = hand
        hand_dict[line.split(" ")[0].strip()]["bid"] = bid

    # First sorting pass
    for key in hand_dict.keys():
        a, counts = np.unique(hand_dict[key]["hand"], return_counts=True)
        if 1 in a:
            jokers = counts[0]
            counts[0] = 0
        else:
            jokers = 0
        if max(counts) + jokers == 5:  # five of a kind
            hand_dict[key]["type"] = 1
        elif max(counts) + jokers == 4:  # four of a kind
            hand_dict[key]["type"] = 2
        elif (3 in counts and 2 in counts) or (
            np.count_nonzero(counts == 2) == 2 and jokers == 1
        ):  # full house
            hand_dict[key]["type"] = 3
        elif max(counts) + jokers == 3:  # three of a kind
            hand_dict[key]["type"] = 4
        elif (np.count_nonzero(counts == 2) == 2) or (
            np.count_nonzero(counts == 2) == 1 and jokers == 1
        ):  # two pair
            hand_dict[key]["type"] = 5
        elif max(counts) + jokers == 2:  # pair
            hand_dict[key]["type"] = 6
        else:  # high card
            hand_dict[key]["type"] = 7

    # Second sorting
    prev_index = 0
    for typei in range(1, 8):
        type_hands = []
        keys = []
        for key in hand_dict.keys():
            if hand_dict[key]["type"] == typei:
                type_hands.append(hand_dict[key]["hand"])
                keys.append(key)

        indices = sorted(
            range(len(type_hands)), key=lambda k: type_hands[k], reverse=True
        )

        for rank, i in enumerate(indices):
            hand_dict[keys[i]]["type_rank"] = prev_index + rank
            hand_dict[keys[i]]["total_rank"] = (
                hand_dict[keys[i]]["type"] * len(hand_dict)
                + hand_dict[keys[i]]["type_rank"]
            )

        prev_index += len(indices)

    to_sort = [
        (
            hand_dict[key]["total_rank"],
            hand_dict[key]["bid"],
            key,
            hand_dict[key]["hand"],
            hand_dict[key]["type"],
        )
        for key in hand_dict.keys()
    ]

    # Sort in reverse, as for us lowest value is best
    to_sort = sorted(to_sort, key=lambda k: k[0], reverse=True)

    total = 0
    for i, val in enumerate(to_sort):
        total += val[1] * (i + 1)  #

    return total


if __name__ == "__main__":
    with open("data/day7.txt") as file:
        lines = list(file)
        part1_ans = part1(lines)
        part2_ans = part2(lines)
        print(f"Answer for Part 1: {part1_ans}")
        print(f"Answer for Part 2: {part2_ans}")
