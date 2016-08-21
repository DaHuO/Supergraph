import sys

f = open(sys.argv[1], 'r')

cases = int(f.readline())
case = 1

for line in f:
    states = set()
    base = int(line)

    state = base

    if base == 0:
        result = 'INSOMNIA'
    else:
        while True:
            for char in str(state):
                states.add(char)

            if len(states) == 10:
                break

            state += base
        result = state

    print 'Case #{}: {}'.format(case, result)

    case += 1
