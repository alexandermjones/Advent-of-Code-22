# Standard library imports
from pathlib import Path

# Local imports
import utils

# Global variables
DAY = 2
TEST_ANSWER_ONE = 15
TEST_ANSWER_TWO = 12

WIN_DICT = {'A': 'Y', 'B': 'Z', 'C': 'X'}
TIE_DICT = {'A': 'X', 'B': 'Y', 'C': 'Z'}
LOSE_DICT = {'A': 'Z', 'B': 'X', 'C': 'Y'}


def score(round: list):
    if round[1] == 'X':
        score = 1
    elif round[1] == 'Y':
        score = 2
    else:
        score = 3
    if tuple(round) in WIN_DICT.items():
        score += 6
    elif tuple(round) in TIE_DICT.items():
        score += 3
    return score


def convert_move(round: list):
    if round[1] == 'X':
        round[1] = LOSE_DICT[round[0]]
    elif round[1] == 'Y':
        round[1] = TIE_DICT[round[0]]
    else:
        round[1] = WIN_DICT[round[0]]
    return round


def solve_part_one(lines: list):
    total_score = 0
    for line in lines:
        round = line.split()
        total_score += score(round)
    return total_score


def solve_part_two(lines: list):
    total_score = 0
    for line in lines:
        round = line.split()
        round = convert_move(round)
        total_score += score(round)
    return total_score


if __name__ == "__main__":
    utils.test_print_part(solve_part_one, DAY, 1, TEST_ANSWER_ONE)
    utils.test_print_part(solve_part_two, DAY, 2, TEST_ANSWER_TWO)
