

def solution(N):
    if N == 0: return 'INSOMNIA'
    seen = [0] * 10
    done = 0
    counter = 0
    while True:
        n = str((counter + 1) * N)
        for x in n:
            x = int(x)
            if seen[x] == 0:
                seen[x] = 1
                done += 1
        if done == 10:
            last = n
            break
        counter += 1
    return last


def file_reader(file_name):
    case = 0
    with open(file_name) as infile:
        for line in infile:
            if case == 0:
                case += 1
                continue
            s = solution(int(line))
            with open('small-output', 'a') as the_file:
                the_file.write('Case #' + str(case) + ': ' + s + '\n')
            case += 1


file_reader('A-small-attempt0.in')
