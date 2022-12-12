# Local imports
import utils

# Global variables
DAY = 7
TEST_ANSWER_ONE = 95437
TEST_ANSWER_TWO = None


class Dir:
    def __init__(self, id, parent):
        self.id = id
        self.parent = parent
        self.files = dict()
        self.dirs = set()
    

    def size(self):
        print(self.id)
        size_files = sum(self.files.values())
        size_dirs = size_files
        for dir in self.dirs:
            size_dirs += dir.size()
        return size_dirs
    

    def list_dir_ids(self):
        dirs = [dir.id for dir in self.dirs]
        for dir in self.dirs:
            dirs += dir.list_dir_ids()
        return dirs


def parse_input(lines: list):
    dirs = {'/': Dir('/', '/')}
    current_dir = dirs['/']
    for line in lines:
        if line.startswith('$ cd'):
            id = line.split('$ cd ')[1]
            if id == '..':
                current_dir = dirs[current_dir.parent]
            else:
                current_dir = dirs[id]
        elif line.startswith('$ ls'):
            pass
        elif line.startswith('dir '):
            id = line.split('dir ')[1]
            if not id in dirs:
                dirs[id] = Dir(id, current_dir.id)
            if not id in current_dir.dirs:
                current_dir.dirs.add(dirs[id])
        elif line.strip():
            size, id = line.split()
            if not id in current_dir.files:
                current_dir.files[id] = int(size)
    return dirs


def solve_part_one(lines: list):
    dirs = parse_input(lines)
    size = 0
    for dir in dirs.values():
        if dir.id != '/' and dir.size() <= 100000:
            print(dir.id, dir.size())
            size += dir.size()
            print(size)
            if dir.id == "clm":
                raise AssertionError
    return size


def solve_part_two(lines: list):
    pass


if __name__ == "__main__":
    utils.test_print_part(solve_part_one, DAY, 1, TEST_ANSWER_ONE)
    utils.test_print_part(solve_part_two, DAY, 2, TEST_ANSWER_TWO)
