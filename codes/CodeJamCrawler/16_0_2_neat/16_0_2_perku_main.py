def reader(input_file):
    with open(input_file) as f:
        len_cases = int(f.readline())
        cases = []
        for case in xrange(len_cases):
            cases.append(f.readline().strip())
        return cases


def maneuver(pancakes):
    pancakes.reverse()
    return map(lambda x: '+' if x == '-' else '-', pancakes)


def solver(pancakes):
    maneuvers = 0
    while '-' in pancakes:
        if '+' not in pancakes:
            return maneuvers + 1

        if pancakes[0] == '-':
            j = pancakes.index('+')
            pancakes[:j] = maneuver(pancakes[:j])
            maneuvers += 1
        else:
            j = pancakes.index('-')
            pancakes[:j] = maneuver(pancakes[:j])
            maneuvers += 1

    return maneuvers

cases = reader('large.in')
for i, case in enumerate(cases):
    result = solver(list(case))
    print 'Case #{}: {}'.format(i+1, result)

