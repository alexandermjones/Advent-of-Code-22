"""
Standard utilities for Advent of Code puzzles.
"""

# Standard library imports
from pathlib import Path
from typing import Any, Callable


def open_input(day, test:bool=False) -> list:
    """
    Load input data and convert into a list of strings for each new line.

    Args:
        test (bool, default=False): Whether data is test data or actual input data.
    
    Returns:
        list: list of individual lines (strs)
    """
    if test:
        input_fpath = Path(__file__).parent.parent / 'inputs' / f'{day}_test.txt'
    else:
        input_fpath = Path(__file__).parent.parent / 'inputs' / f'{day}_input.txt'
    with open(input_fpath, 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines


def test_print_part(solution_func: Callable, day: int, part: int, test_answer: Any) -> None:
    """
    Test and print the solution to an advent of code puzzle.

    Args:
        solution_func (Callable): The function to solve puzzle.
        day (int): The day of the puzzle.
        part (int): The part of the puzzle.
        test_answer (Any): The test answer to the puzzle.
    """
    test_lines = open_input(day, test=True)
    actual_lines = open_input(day)
    try:
        attempt_test_answer = solution_func(test_lines)
        assert test_answer == attempt_test_answer
    except AssertionError:
        print(f'Error with test data for part {part}. Expected: {test_answer}, actual: {attempt_test_answer}.')
    answer = solution_func(actual_lines)
    print(f'Answer to day {day}, part {part} is: {answer}.')
    return None
