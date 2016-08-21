from itertools import product


def get_values(candidate):
    ret = []
    for i in range(2, 11):
        ret.append(int(candidate, i))
    return ret


def not_prime_maybe(num):
    test = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    for t in test:
        if num % t == 0:
            return t
    return False


def is_valid(candidate):
    bases = get_values(candidate)
    pppp = map(not_prime_maybe, bases)
    if all(pppp):
        return pppp


def solve(n, j):
    found = []
    for i in product([0, 1], repeat=n - 2):
        candidate = '1' + ''.join(map(str, i)) + '1'
        ret = is_valid(candidate)
        if ret:
            yep = [candidate] + ret
            # print yep
            found.append(yep)

        if len(found) >= j:
            return found
    return found


t = int(raw_input())

for c in range(t):
    line = raw_input().split()
    n, j = map(int, line)

    print "Case #{}: ".format(str(c + 1))
    for res in solve(n, j):
        print ' '.join([str(x) for x in res])
