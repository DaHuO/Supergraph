

def turn_hotcackes(S, steps, current):
    for idx, x in enumerate(S):
        if S[idx] != current:
            current = S[idx]
            for x in xrange(idx, -1, -1):
                S[x] = current
            steps += 1
    if '+' not in S:
        for x in xrange(len(S)):
            S[x] = '+'
        steps += 1
    return steps


def solution(S):
    S = list(S)
    if '-' not in S: return 0
    current = S[0]
    steps = 0
    steps = turn_hotcackes(S, steps, current)
    return steps

def file_reader(file_name):
    case = 0
    with open(file_name) as infile:
        for line in infile:
            if case == 0:
                case += 1
                continue
            s = solution(line.strip())
            with open('small-output', 'a') as the_file:
                the_file.write('Case #' + str(case) + ': ' + str(s) + '\n')
            case += 1



file_reader('B-small-attempt0.in')
