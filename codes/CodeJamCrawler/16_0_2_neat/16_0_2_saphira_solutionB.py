def getInput(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    return lines


def print_ouput():
    lines = getInput("inputB.txt")
    no_cases = int(lines[0].strip())
    case = 1
    while case <= no_cases:
        sol = get_solution(lines[case].strip())
        print "Case #{0}: {1}".format(case, sol)
        case += 1

"""
def get_solution(stack):
    count = 0
    curr_top_pattern = stack[0]
    while True:
        if check_if_done(stack) is True:
            return count
        index = get_first_change_point(stack)
        #turning till index-1
        curr_top_pattern = "+" if curr_top_pattern == "-" else "-"
        stack = curr_top_pattern*index + stack[index:]
        count += 1

def get_first_change_point(stack):
    pattern = stack[0]
    for index, cake in enumerate(stack):
        if cake != pattern:
            return index
    return len(stack)


def check_if_done(stack):
    if "-" in stack:
        return False
    return True
"""


def get_solution(stack):
    curr_pattern = stack[0]
    num_of_changes = 0
    for cake in stack:
        if curr_pattern != cake:
            num_of_changes += 1
        curr_pattern = cake
    if num_of_changes % 2 == 1 and stack[0] == "+":
        return num_of_changes + 1
    elif num_of_changes % 2 == 0 and stack[0] == "-":
        return num_of_changes + 1
    else:
        return num_of_changes


print_ouput()