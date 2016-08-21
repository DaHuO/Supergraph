import copy
import sys


def getInput(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    return lines


def print_ouput():
    input_file_name = sys.argv[1]
    lines = getInput(input_file_name)
    no_cases = int(lines[0].strip())
    case = 1
    while case <= no_cases:
        sol = get_solution(lines[2*case - 1].strip(), lines[2*case].strip())
        print "Case #{0}: {1}".format(case, sol)
        case += 1


def get_solution(count, count_type):
    count = int(count)
    count_type = [int(x) for x in count_type.split()]
    return_val = ""
    alpha_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
                  "Y", "Z"]
    input_dict = {}
    for i in xrange(0, count):
        input_dict[alpha_list[i]] = count_type[i]
    curr_dict = copy.deepcopy(input_dict)
    while True:
        max_cases = get_max_cases(curr_dict)
        #special case
        if len(max_cases) == 2 and len(curr_dict) == 2:
            return_val += "{0}{1} ".format(max_cases[0], max_cases[1])
            curr_dict[max_cases[0]] -= 1
            curr_dict[max_cases[1]] -= 1
            if curr_dict[max_cases[0]] == 0:
                curr_dict.pop(max_cases[0])
            if curr_dict[max_cases[1]] == 0:
                curr_dict.pop(max_cases[1])
        else:
            return_val += "{0} ".format(max_cases[0])
            curr_dict[max_cases[0]] -= 1
            if curr_dict[max_cases[0]] == 0:
                curr_dict.pop(max_cases[0])
        #if all([x == 0 for x in curr_dict.values()]) is True:
        #    break
        if len(curr_dict) == 0:
            break
    return return_val.strip()


def get_max_cases(curr_dict):
    max_list = []
    max = 0
    for item, count in curr_dict.items():
        if count > max:
            max_list = [item]
            max = count
        elif count == max:
            max_list.append(item)
    return max_list



print_ouput()