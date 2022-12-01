# Standard library imports
from pathlib import Path

# Global variables
DAY = 1
TEST_ANSWER_ONE = 24000
TEST_ANSWER_TWO = 45000


def open_input(test:bool=False):
    if test:
        input_fpath = Path.cwd().parent / 'inputs' / f'{DAY}_test.txt'
    else:
        input_fpath = Path.cwd().parent / 'inputs' / f'{DAY}_input.txt'
    with open(input_fpath, 'r') as f:
        lines = f.readlines()
    return lines


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


def solve_day_part_one(lines: list):
    total_calories = get_carry_totals(lines)
    max_total_calories = max(total_calories)
    return max_total_calories


def solve_day_part_two(lines: list):
    total_calories = get_carry_totals(lines)
    total_calories.sort(reverse=True)
    sum_top_three = sum(total_calories[:3])
    return sum_top_three


def test_and_print_day():
    test_lines = open_input(test=True)
    actual_lines = open_input()
    try:
        test_answer_part_one = solve_day_part_one(test_lines)
        assert test_answer_part_one == TEST_ANSWER_ONE
    except AssertionError:
        print(f'Error with test data. Expected: {TEST_ANSWER_ONE}, actual: {test_answer_part_one}.')
    part_one_answer = solve_day_part_one(actual_lines)
    if part_one_answer:
        print(f'Answer to day {DAY}, part 1 is: {part_one_answer}')
    try:
        test_answer_part_two = solve_day_part_two(test_lines)
        assert test_answer_part_two == TEST_ANSWER_TWO
    except AssertionError:
        print(f'Error with test data. Expected: {TEST_ANSWER_TWO}, actual: {test_answer_part_two}.')
    part_two_answer = solve_day_part_two(actual_lines)
    if part_two_answer:
        print(f'Answer to day {DAY}, part 2 is: {part_two_answer}')


if __name__ == "__main__":
    test_and_print_day()
