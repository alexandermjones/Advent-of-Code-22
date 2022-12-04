# Standard library imports
from pathlib import Path

# Local imports
import utils

# Global variables
DAY = 4
TEST_ANSWER_ONE = 2
TEST_ANSWER_TWO = 4


def get_pairs(lines: list):
    pairs = []
    for line in lines:
        pair = line.split(',')
        pair = [_.split('-') for _ in pair]
        pair = [[int(x) for x in y] for y in pair]
        pairs.append(pair)
    return pairs


def solve_part_one(lines: list):
    contained = 0
    pairs = get_pairs(lines)
    for pair in pairs:
        if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
            contained += 1
        elif pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
            contained += 1
    return contained


def solve_part_two(lines: list):
    overlap = 0
    pairs = get_pairs(lines)
    for pair in pairs:
        if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][0]:
            overlap += 1
        elif pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][0]:
            overlap += 1
    return overlap


if __name__ == "__main__":
    utils.test_print_part(solve_part_one, DAY, 1, TEST_ANSWER_ONE)
    utils.test_print_part(solve_part_two, DAY, 2, TEST_ANSWER_TWO)
