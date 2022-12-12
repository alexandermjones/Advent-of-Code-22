from math import prod

# Local imports
import utils

# Global variables
DAY = 10
TEST_ANSWER_ONE = 13140
TEST_ANSWER_TWO = None


#with open('10_p2_test_ans.txt', 'r') as f:
#    img = f.readlines()


def process_input(line, last_cycle, cycles):
    cycles[last_cycle+1] = cycles[last_cycle]
    last_cycle += 1
    if line.startswith('addx'):
        value = int(line.split()[1])
        cycles[last_cycle+1] = cycles[last_cycle] + value
        last_cycle += 1
    return cycles, last_cycle


def solve_part_one(lines: list):
    signal_strengths = []
    cycles = {1: 1}
    last_cycle = 1
    for line in lines:
        cycles, last_cycle = process_input(line, last_cycle, cycles)
    for i in range(1,241):
        if i % 40 == 0:
            strength = cycles[i-20]
            signal_strengths.append(strength*(i-20))
    return sum(signal_strengths)


def solve_part_two(lines: list):
    signal_strengths = []
    cycles = {1: 1}
    last_cycle = 1
    for line in lines:
        cycles, last_cycle = process_input(line, last_cycle, cycles)
    output_lines = []
    output = ''
    for cycle, val in cycles.items():
        if cycle == 1:
            output += '#'
            continue
        pos = cycle % 40
        if pos in [val, val+1, val+2]:
            output += '#'
        else:
            output += '.'
        if cycle % 40 == 0:
            output_lines.append(output)
            output = ''
    for line in output_lines:
        print(line)
    return output_lines


if __name__ == "__main__":
    utils.test_print_part(solve_part_one, DAY, 1, TEST_ANSWER_ONE)
    solve_part_two(utils.open_input(DAY, test=True))
    print('\n\n')
    solve_part_two(utils.open_input(DAY))
