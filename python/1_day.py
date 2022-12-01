# Standard library imports
from pathlib import Path

# Local imports
import utils

# Global variables
DAY = 1
TEST_ANSWER_ONE = 24000
TEST_ANSWER_TWO = 45000


def get_carry_totals(lines):
    totals = []
    calories = []
    for line in lines:
        if line.strip():
            calories.append(int(line))
        else:
            totals.append(calories)
            calories = []
    totals.append(calories)
    total_calories = [sum(cals) for cals in totals]
    return total_calories


def solve_part_one(lines: list):
    total_calories = get_carry_totals(lines)
    max_total_calories = max(total_calories)
    return max_total_calories


def solve_part_two(lines: list):
    total_calories = get_carry_totals(lines)
    total_calories.sort(reverse=True)
    sum_top_three = sum(total_calories[:3])
    return sum_top_three


if __name__ == "__main__":
    utils.test_print_part(solve_part_one, DAY, 1, TEST_ANSWER_ONE)
    utils.test_print_part(solve_part_two, DAY, 2, TEST_ANSWER_TWO)
