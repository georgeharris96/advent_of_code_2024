from collections import Counter

def import_input(run=True):
    if run:
        with open("day-1/day-1-input.txt") as file:
            lines = [line.strip("\n").split("   ") for line in file.readlines()]

        list_1, list_2 = [], []
        for line in lines:
            list_1.append(int(line[0]))
            list_2.append(int(line[1]))

        assert len(list_1) == len(list_2)
        return list_1, list_2
    else:
        return [3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]

def calculate_distance(list_1, list_2):
    list_1.sort()
    list_2.sort()
    total_distance = 0
    for i in range(len(list_1)):
        total_distance += abs(list_1[i]-list_2[i])

    print(f"total_distance: {total_distance}")
    return total_distance

def calculate_similarity(list_1, list_2):
    total_similarity = 0
    for number in list_1:
        total_similarity += Counter(list_2)[number] * number
    print(f"total_similarity: {total_similarity}")

def main():
    left_list, right_list = import_input()
    total_distance = calculate_distance(left_list, right_list)
    total_similarity = calculate_similarity(left_list, right_list)

main()
