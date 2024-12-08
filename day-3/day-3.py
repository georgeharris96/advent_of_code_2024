import re
def import_input(run=True):
    if run:
        with open('day-3/day-3-input.txt') as file:
            lines = [line for line in file.readlines()]
    else:
        lines = ['xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))']
    return lines

def find_muls(lines):
    muls = []
    for line in lines:
        muls.append(re.findall(r'mul\((-?\d+),(-?\d+)\)',line))
    return muls

def calc_muls(list_of_muls):
    sum_of_muls = 0
    for muls in list_of_muls:
        for mul in muls:
            sum_of_muls += int(mul[0])*int(mul[1])
    print(f"sum_of_muls: {sum_of_muls}")
    return sum_of_muls

def main():
    lines = import_input()
    list_of_muls = find_muls(lines)
    sum_of_muls = calc_muls(list_of_muls)

main()