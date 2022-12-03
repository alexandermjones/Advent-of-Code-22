# Standard library imports
from pathlib import Path

# Local imports
import utils

# Global variables
DAY = 3
TEST_ANSWER_ONE = 157
TEST_ANSWER_TWO = 70


def find_common_items(lines: list):
    common_items = []
    for line in lines:
        line = line.strip()
        compartment_length = int(len(line)/2)
        compart_one = set(line[:compartment_length])
        compart_two = set(line[compartment_length:])
        common_items.append(compart_one.intersection(compart_two).pop())
    return common_items


def get_common_items_group(lines: list):
    common_items = []
    lines = [line.strip() for line in lines]
    groups = [lines[_*3:_*3+3] for _ in range(int(len(lines)/3))]
    for group in groups:
        common_item = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
        common_items.append(common_item.pop())
    return common_items


def item_val(char: str):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96


def solve_part_one(lines: list):
    common_items = find_common_items(lines)
    item_vals = [item_val(char) for char in common_items]
    return sum(item_vals)


def solve_part_two(lines: list):
    common_items = get_common_items_group(lines)
    item_vals = [item_val(char) for char in common_items]
    return sum(item_vals)    


if __name__ == "__main__":
    utils.test_print_part(solve_part_one, DAY, 1, TEST_ANSWER_ONE)
    utils.test_print_part(solve_part_two, DAY, 2, TEST_ANSWER_TWO)
