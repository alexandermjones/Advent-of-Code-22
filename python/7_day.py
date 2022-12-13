# Local imports
import utils

# Global variables
DAY = 7
TEST_ANSWER_ONE = 95437
TEST_ANSWER_TWO = 24933642


def parse_input(lines):
    dirs = {'/': 0}
    dirs_tracking = ['/']
    for line in lines:
        if line.startswith('$ cd'):
            id = line.split()[2]
            if id == '/':
                dirs_tracking = ['/']
            elif id == '..':
                dirs_tracking.pop()
            else:
                full_id = '.'.join(dirs_tracking) + f'.{id}'
                dirs[full_id] = 0
                dirs_tracking.append(full_id)
        elif line.startswith('$ ls'):
            continue
        elif line.startswith('dir'):
            continue
        else:
            size = line.split()[0]
            for dir in dirs_tracking:
                dirs[dir] += int(size)
    return dirs


def solve_part_one(lines: list):
    size = 0
    dirs = parse_input(lines)
    for dir in dirs:
        if dirs[dir] < 100000:
            size += dirs[dir]
    return size


def solve_part_two(lines: list):
    dirs = parse_input(lines)
    space_available = 70000000 - dirs['/']
    space_required = 30000000 - space_available
    candidate_dir = '/'
    for dir in dirs:
        if dirs[dir] >= space_required and dirs[dir] < dirs[candidate_dir]:
            candidate_dir = dir
    return dirs[candidate_dir]


if __name__ == "__main__":
    utils.test_print_part(solve_part_one, DAY, 1, TEST_ANSWER_ONE)
    utils.test_print_part(solve_part_two, DAY, 2, TEST_ANSWER_TWO)
