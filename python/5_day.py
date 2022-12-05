# Standard library imports
from collections import deque

# Local imports
import utils

# Global variables
DAY = 5
TEST_ANSWER_ONE = 'CMZ'
TEST_ANSWER_TWO = 'MCD'


def parse_input(lines: list):
    for i, line in enumerate(lines):
        if line.strip().startswith('1'):
            column_line_end = i
            column_ints = line
        if line.startswith('move'):
            instruction_start_line = i
            break
    columns = lines[:column_line_end]
    instructions = lines[instruction_start_line:]
    num_cols = int(column_ints.strip()[-1])
    return columns, num_cols, instructions


def columns_to_deques(columns: list, num_cols: int):
    deqs = {i: deque() for i in range(1, num_cols+1)}
    for line in reversed(columns):
        entries = [char for i, char in enumerate(line) if (i-1)%4 == 0]
        for i, entry in enumerate(entries):
            if entry.strip():
                deqs[i+1].append(entry)
    return deqs


def follow_instruction(deqs, instruction, partone=True):
    words = instruction.split()
    num_move = int(words[1])
    deq_from = int(words[3])
    deq_to = int(words[5])
    if partone:
        for i in range(num_move):
            deqs[deq_to].append(deqs[deq_from].pop())
    else:
        items_to_add = []
        for i in range(num_move):
            items_to_add.append(deqs[deq_from].pop())
        deqs[deq_to].extend(reversed(items_to_add))
    return deqs


def solve_part_one(lines: list):
    columns, num_cols, instructions = parse_input(lines)
    deqs = columns_to_deques(columns, num_cols)
    for instruction in instructions:
        deqs = follow_instruction(deqs, instruction)
    top_of_deq = ''
    for deq in deqs.values():
        top_of_deq += deq.pop()
    return top_of_deq


def solve_part_two(lines: list):
    columns, num_cols, instructions = parse_input(lines)
    deqs = columns_to_deques(columns, num_cols)
    for instruction in instructions:
        deqs = follow_instruction(deqs, instruction, partone=False)
    top_of_deq = ''
    for deq in deqs.values():
        top_of_deq += deq.pop()
    return top_of_deq


if __name__ == "__main__":
    utils.test_print_part(solve_part_one, DAY, 1, TEST_ANSWER_ONE,strip_lines=False)
    utils.test_print_part(solve_part_two, DAY, 2, TEST_ANSWER_TWO, strip_lines=False)
