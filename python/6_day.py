# Local imports
import utils

# Global variables
DAY = 6
TEST_ANSWER_ONE = 7
TEST_ANSWER_TWO = 19


def find_marker(line: str, length: int):
    for i in range(len(line)):
        if len(set(line[i:i+length])) == len(line[i:i+length]):
            return i + length
    return None


def solve_part_one(lines: list):
    line = lines[0]
    return find_marker(line, 4)


def solve_part_two(lines: list):
    line = lines[0]
    return find_marker(line, 14)


if __name__ == "__main__":
    utils.test_print_part(solve_part_one, DAY, 1, TEST_ANSWER_ONE)
    utils.test_print_part(solve_part_two, DAY, 2, TEST_ANSWER_TWO)
