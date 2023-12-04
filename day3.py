import re


# Part one
def part1(lines: list):
    total = 0
    all_line_ids = []
    numbers_and_spans = []
    # Collect all numbers, symbols and their spans per line
    for line in lines:
        symbols = re.finditer(
            r"[^0-9\.\s]", line
        )  # find everything that is not a number or .
        numbers = re.finditer(r"\d+", line)  # find all the numbers
        line_ids = []
        ns_spans = []
        for symbol in symbols:
            line_ids.append(symbol.start())
        for number in numbers:
            actual_number = int(number.group(0))
            span = number.span()
            ns_spans.append((actual_number, span))
        all_line_ids.append(line_ids)
        numbers_and_spans.append(ns_spans)

    for idx, number_line in enumerate(numbers_and_spans):
        print(f"Line id {idx}")
        if idx == 0:
            for number in number_line:
                actual_number = number[0]
                span = number[1]
                counted = False
                for symbol_pos in all_line_ids[0] + all_line_ids[1]:
                    # Check diagonals
                    if span[0] - 1 <= symbol_pos <= span[1]:
                        # count only once
                        if not counted:
                            total += actual_number
                            counted = True

        # Check only backwards
        elif idx == len(numbers_and_spans) - 1:
            for number in number_line:
                actual_number = number[0]
                span = number[1]
                counted = False
                for symbol_pos in all_line_ids[idx - 1] + all_line_ids[idx]:
                    # Check diagonals
                    if span[0] - 1 <= symbol_pos <= span[1]:
                        # count only once
                        if not counted:
                            total += actual_number
                            counted = True
        # Check both backwards and forwards
        else:
            for number in number_line:
                actual_number = number[0]
                span = number[1]
                counted = False
                for symbol_pos in (
                    all_line_ids[idx - 1] + all_line_ids[idx] + all_line_ids[idx + 1]
                ):
                    # Check diagonals
                    if span[0] - 1 <= symbol_pos <= span[1]:
                        # count only once
                        if not counted:
                            total += actual_number
                            counted = True
    return total


# Part two
def part2(lines: list):
    total = 0
    all_line_ids = []
    numbers_and_spans = []
    # Collect all numbers, symbols and their spans per line
    for line in lines:
        symbols = re.finditer(
            r"[\*]", line
        )  # find everything that is not a number or .
        numbers = re.finditer(r"\d+", line)  # find all the numbers
        line_ids = []
        ns_spans = []
        for symbol in symbols:
            line_ids.append(symbol.start())
        for number in numbers:
            actual_number = int(number.group(0))
            span = number.span()
            ns_spans.append((actual_number, span))
        all_line_ids.append(line_ids)
        numbers_and_spans.append(ns_spans)

    for idx, symbols in enumerate(all_line_ids):
        # Check only forwards
        print(f"Line id {idx}")
        if idx == 0:
            for symbol in symbols:
                adjacent_numbers = []
                for number in numbers_and_spans[0] + numbers_and_spans[1]:
                    span = number[1]
                    if span[0] - 1 <= symbol <= span[1]:
                        adjacent_numbers.append(number[0])
                if len(adjacent_numbers) == 2:
                    total += adjacent_numbers[0] * adjacent_numbers[1]

        # Check only backwards
        elif idx == len(numbers_and_spans) - 1:
            for symbol in symbols:
                adjacent_numbers = []
                for number in numbers_and_spans[idx - 1] + numbers_and_spans[idx]:
                    span = number[1]
                    if span[0] - 1 <= symbol <= span[1]:
                        adjacent_numbers.append(number[0])
                if len(adjacent_numbers) == 2:
                    total += adjacent_numbers[0] * adjacent_numbers[1]

        # Check both backwards and forwards
        else:
            for symbol in symbols:
                adjacent_numbers = []
                for number in (
                    numbers_and_spans[idx - 1]
                    + numbers_and_spans[idx]
                    + numbers_and_spans[idx + 1]
                ):
                    span = number[1]
                    if span[0] - 1 <= symbol <= span[1]:
                        adjacent_numbers.append(number[0])
                if len(adjacent_numbers) == 2:
                    total += adjacent_numbers[0] * adjacent_numbers[1]

    return total


if __name__ == "__main__":
    with open("data/day3.txt") as file:
        lines = list(file)
        part1_ans = part1(lines)
        part2_ans = part2(lines)
        print(f"Answer for Part 1: {part1_ans}")
        print(f"Answer for Part 2: {part2_ans}")
