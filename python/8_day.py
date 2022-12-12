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
        self.scenic = 0


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


def get_scenic_score(rows, i, j):
    visible_left = 0
    for tree in range(j-1, -1, -1):
        visible_left += 1
        if rows[i][j].height <= rows[i][tree].height:
            break
    visible_right = 0
    for tree in range(j+1, len(rows[i])):
        visible_right += 1
        if rows[i][j].height <= rows[i][tree].height:
            break
    visible_top = 0
    for tree in range(i-1, -1, -1):
        visible_top += 1
        if rows[i][j].height <= rows[tree][j].height:
            break
    visible_bottom = 0
    for tree in range(i+1, len(rows)):
        visible_bottom += 1
        if rows[i][j].height <= rows[tree][j].height:
            break
    scenic_score = visible_left * visible_right * visible_top * visible_bottom
    return scenic_score


def set_scenic_scores(rows: list):
    for i, row in enumerate(rows):
        if i == 0 or i == len(rows):
            continue
        for j in range(len(row)-1):
            if j == 0:
                continue
            rows[i][j].scenic = get_scenic_score(rows, i, j)


def solve_part_one(lines: list):
    rows, cols = parse_input(lines)
    check_rows(rows, cols)
    visible_trees = [[1 for tree in row if tree.visible] for row in rows]
    summed_visible = [sum(row) for row in visible_trees]
    return sum(summed_visible)


def solve_part_two(lines: list):
    rows, _ = parse_input(lines)
    set_scenic_scores(rows)
    top_scenic = max([max([tree.scenic for tree in row]) for row in rows])
    return top_scenic


if __name__ == "__main__":
    utils.test_print_part(solve_part_one, DAY, 1, TEST_ANSWER_ONE)
    utils.test_print_part(solve_part_two, DAY, 2, TEST_ANSWER_TWO)
