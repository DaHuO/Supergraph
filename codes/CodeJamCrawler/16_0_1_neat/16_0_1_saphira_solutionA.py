def getInput(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    return lines


def print_ouput():
    lines = getInput("inputA.txt")
    no_cases = int(lines[0].strip())
    case = 1
    while case <= no_cases:
        sol = get_solution(lines[case])
        print "Case #{0}: {1}".format(case, sol)
        case += 1


def get_solution(num):
    num = int(num)
    if num == 0:
        return "INSOMNIA"
    done_map = {str(x): 0 for x in xrange(0, 10)}
    present_num = num
    while True:
        for digit in str(present_num):
            done_map[digit] = 1
        if all(done_map.values()) is True:
            return present_num
        present_num += num


print_ouput()