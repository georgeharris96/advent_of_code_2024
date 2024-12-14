import re
from itertools import chain

def import_input(run=True):
    if run:
        with open('day-3/day-3-input.txt') as file:
            lines = [line.strip("\n") for line in file.readlines()]
    else:
        lines = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
    return "".join(lines)

def filter_text(text):
    filtered_text = []
    for segment in text.split("do()"):
        filtered_text.append(segment.split("don't()")[0])
    return filtered_text[0]

def find_mul_statements(text):
    mul_statements = re.findall(r'mul\((-?\d+),(-?\d+)\)', text)
    return mul_statements

def calculate_answer(mul_statements):
    answer = 0
    for statement in mul_statements:
        answer += int(statement[0]) * int(statement[1])
    
    print(f"Answer: {answer}")
    return answer

def main():
    text = import_input()
    filtered_text = filter_text(text)
    mul_statements = find_mul_statements(filtered_text)
    answer = calculate_answer(mul_statements)

main()
