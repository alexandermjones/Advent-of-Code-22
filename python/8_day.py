# Local imports
import utils

# Global variables
DAY = 8
TEST_ANSWER_ONE = 21
TEST_ANSWER_TWO = 8


class Tree():
    def __init__(self, height):
        self.height = int(height)
        self.visible = False
        self.scenics = (0,0,0,0)


def parse_input(lines: list):
    rows = [[Tree(line[i]) for i in range(len(lines[0]))] for line in lines]
    cols = [[row[i] for row in rows] for i in range(len(lines[0]))]
    return rows, cols


def check_visible(tree, trees: list):
    if tree.height > max([tree.height for tree in trees], default=-1):
        tree.visible = True


def check_rows(rows: list, cols: list):
    for row in rows:
        for i, tree in enumerate(row):
            check_visible(tree, row[:i])
            check_visible(tree, row[i+1:])
    for col in cols:
        for i, tree in enumerate(col):
            check_visible(tree, col[:i])
            check_visible(tree, col[i+1:])


def solve_part_one(lines: list):
    rows, cols = parse_input(lines)
    check_rows(rows, cols)
    visible_trees = [[1 for tree in row if tree.visible] for row in rows]
    summed_visible = [sum(row) for row in visible_trees]
    return sum(summed_visible)


def solve_part_two(lines: list):
    pass


if __name__ == "__main__":
    utils.test_print_part(solve_part_one, DAY, 1, TEST_ANSWER_ONE)
    utils.test_print_part(solve_part_two, DAY, 2, TEST_ANSWER_TWO)
