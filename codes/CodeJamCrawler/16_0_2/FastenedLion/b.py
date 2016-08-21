HAPPY = '+'
SAD = '-'


def flip(pancakes):
    return [HAPPY if p == SAD else SAD for p in pancakes][::-1]


def get_last_sad_index(pancakes):
    for i, p in enumerate(pancakes[::-1], 1):
        if p == SAD:
            return len(pancakes) - i
    return -1


def get_first_sad_index(pancakes):
    try:
        return pancakes.index(SAD)
    except:
        return -1

def solve(pancakes):
    result = 0
    pancakes = list(pancakes.strip())
    print ''.join(pancakes)
    while pancakes:
        last_sad = get_last_sad_index(pancakes)
        if last_sad == -1:
            print result
            return result
        pancakes = pancakes[0:last_sad + 1]
        # Flip the top ones so that we get a happy on the bottom.
        first_sad = get_first_sad_index(pancakes)
        if first_sad > 0:
            pancakes[0:first_sad] = [SAD] * first_sad
            result += 1
        pancakes = flip(pancakes)
        result += 1
    print result
    return result


def read_input():
    with open('B-large.in') as f:
        lines = list(f)
    # Skip the number of examples.
    instances = lines[1:]
    with open('output.txt', 'w') as f:
        solns = []
        for case, sol in enumerate(map(solve, instances), 1):
            soln = "Case #%(case)s: %(sol)s" % vars()
            solns.append(soln)
        # Writing output all at once is faster when the list is small.
        f.write('\n'.join(solns))


assert solve('-') == 1
assert solve('-+') == 1
assert solve('+-') == 2
assert solve('+++') == 0
assert solve('--+-') == 3
assert solve('----+----') == 3
read_input()
