
def solve_for_plus(line):
    if len(line) == 1:
        if line[0] == '+':
            return 0
        else:
            return 1
    if line[len(line)-1] == '+':
        return solve_for_plus(line[0:len(line)-1])
    else:
        return solve_for_minus(line[0:len(line)-1]) + 1


def solve_for_minus(line):
    if(len(line) == 1):
        if(line[0] == '-'):
            return 0
        else:
            return 1

    if line[len(line)-1] == '+':
        return solve_for_plus(line[0:len(line)-1]) +1
    else:
        return solve_for_minus(line[0:len(line)-1])

if __name__ == "__main__":
    ip = open("input.txt",'r')
    test_cases = int(ip.readline())
    for i in range(test_cases):
        _line = ip.readline().strip()
        podugu = len(_line)
        if podugu == 1:
            if _line == '+':
                sol = 0
            else:
                sol = 1
        elif _line[podugu-1] == '+':
            sol = solve_for_plus(_line[0:podugu-1])
        else:
            sol = solve_for_minus(_line[0:podugu-1])
            sol = sol+1

        print("Case "+str(i+1)+"#"+str(sol))
