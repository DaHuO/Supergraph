import string


def can_remove_second(tup):
    if len(tup) < 2:
        return False
    toti = sum(map(lambda x: x[0], tup))
    toti2 = toti / 2
    ret = not any(map(lambda x: x[0] > toti2, tup))
    return ret


def solve(n, members):
    labels = string.ascii_uppercase[:n + 1]
    tup = [list(x) for x in sorted(zip(members, labels), reverse=True)]
    rez = ''
    while tup[0][0] != 0:
        tup[0][0] -= 1
        rez+=tup[0][1]
        tup[1][0] -= 1
        if can_remove_second(tup):
            rez+=tup[1][1]
        else:
        	tup[1][0] += 1
        rez+=" "
        tup = sorted(tup, reverse=True)

    return rez


def main():
    num_tests = int(raw_input())
    for i in xrange(num_tests):
        num_parties = int(raw_input())
        members = map(int, raw_input().split())
        print 'Case #{}: {}'.format(i + 1, solve(num_parties, members))
if __name__ == '__main__':
    main()

# 4
# 2
# 2 2
# 3
# 3 2 2
# 3
# 1 1 2
# 3
# 2 3 1
