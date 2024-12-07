def import_input(run=True):
    if run:
        with open("day-2/day-2-input.txt") as file:
            lines = [line.strip("\n").split(" ") for line in file.readlines()]
    else:
        lines = [
             ["7", "6", "4", "2", "1"],
             ["1", "2", "7", "8", "9"],
             ["9", "7", "6", "2", "1"],
             ["1", "3", "2", "4", "5",],
             ["8", "6", "4", "4", "1",], 
             ["1", "3", "6", "7", "9"]
             ]

    lines = [list(map(int, sublist)) for sublist in lines]

    return lines

def _generate_check_lists(report):
    level_changes = []
    level_directions = []
    for i in range(len(report)-1):
        level_changes.append(abs(report[i] - report[i+1]))
        if report[i] > report[i+1]:
            level_directions.append(1)
        if report[i] <= report[i+1]:
            level_directions.append(0)
    return level_directions, level_changes

def report_checker(report):
    safe_report=False

    level_directions, level_changes = _generate_check_lists(report)
    
    if len(report) == sum(level_directions)+1 or sum(report) == 0:
        safe_report=True

        if max(level_changes) <= 3:
            safe_report=True
            
    return safe_report

def problem_dampner(report):
    fixed_report = report

    level_directions, level_changes = _generate_check_lists(report)

    # check and fix direction
    idxs = {
        "down": [i for i, x in enumerate(level_directions) if x == 0],
        "up": [i for i, x in enumerate(level_directions) if x == 1]
        }
    if len(idxs["down"]) == 1:
        del fixed_report[idxs["down"][0]]
        print(fixed_report, report, "removing down")
    
    if len(idxs["up"]) == 1:
        del fixed_report[idxs["up"][0]]
        print(fixed_report, report, "removing up")

    # check and fix levels
    else:
        if any(level_changes) > 3:
            idx = [i for i, x in enumerate(level_changes) if x == max(level_changes)]

            if len(idx) == 1:
                del fixed_report[idx[0]]

    # retest
    return report_checker(fixed_report)

def safety_checks(reports):
    number_of_safe_reports = 0
    safe_reports = []
    for report in reports:
        if report_checker(report):
            number_of_safe_reports += 1
            safe_reports.append(report)
        else:
            if problem_dampner(report):
                number_of_safe_reports += 1
                safe_reports.append(report)
        
    print(safe_reports)
    print(f"number of safe reports:: {number_of_safe_reports}")
    return number_of_safe_reports


def main():
    reports = import_input(run=False)

    number_of_safe_reports = safety_checks(reports)

main()