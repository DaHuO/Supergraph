
def solve_case(case):
    pass

def parse(input_lines):
    n_cases = int(input_lines.pop(0))
    cases = []

    for i in range(len(input_lines)):
        cases.append(input_lines[i].split(' '))

    return n_cases, cases

def solve(input_file):
    with open(input_file + '.in', 'r') as f:
        input_lines = f.read().split('\n')

    n_cases, cases = parse(input_lines)

    solution = []
    for i in range(0, n_cases):
        answer = solve_case(cases[i])
        solution.append('Case #%s: %s' % (i + 1, answer))

    with open(input_file + '.out', 'w') as f:
        f.write('\n'.join(solution))

def jamcoins(size):
    for i in xrange(2**size):
        yield ('1{0:0%sb}1' % size).format(i)

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0 and i != 1 and i != n)))

def factor(n):
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0 and i != 1 and i != n:
            return i

def legit(j):
    divs = []
    for i in range(2, 11):
        value = int(j, i)
        x = factor(value)
        if x is None:
            return None
        else:
            divs.append(str(x))
    return divs

if __name__ == '__main__':
    # for x in range(10):
    #     print '{0}\r'.format(x),
    #     time.sleep(2)

    valid_coins = []
    limit = 50
    ctr = 0
    passes = 0
    for j in jamcoins(14):
        passes += 1
        if ctr >= limit:
            break
        result = legit(j)
        if result:
            print j
            print result
            valid_coins.append((j, result))
            ctr += 1
        print '{0}\r'.format('Checked: %s, Found: %s' % (passes, ctr)),

    solution = []
    for item in valid_coins:
        s = item[0] + ' '
        s += ' '.join(item[1])
        solution.append(s)

    with open('sample' + '.out', 'w') as f:
        f.write('Case #1:\n')
        f.write('\n'.join(solution))

    # solve('problem')

