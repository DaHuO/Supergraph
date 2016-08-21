import sys
def read_case():
    N, K = map(int, raw_input().split())
    Ps = map(float, raw_input().split())
    return N, K, Ps

def evaluate(choice, target):
    if len(choice) == target:
        return reduce(lambda a, b: a*b, choice, 1.0)
    elif target == -len(choice):
        return reduce(lambda a, b: a*(1-b), choice, 1.0)
    else:
        p0 = choice[0]
        choice2 = choice[1:]
        return p0*(evaluate(choice2, target-1)) + (1-p0)*evaluate(choice2, target+1)

def solve(case):
    N, K, Ps = case
    Ps.sort()
    bestp = 0
    for k in range(N):
        if k < K:
            selected = Ps[:k] + Ps[-(K-k):]
            assert len(selected) == K
        else:
            selected = Ps[k-K:k]
            assert len(selected) == K
        p = evaluate(selected, 0)
        bestp = max(p, bestp)
    return bestp

def main(read_case, solve, fmt = 1, debug=False):
    T = int(raw_input())
    for t in range(T):
        sys.stderr.write("%d, " % (t+1))
        case = read_case()
        solution = solve(case)
        if debug:
            print "\+++++++++++++++++++++++++/\n"
            print "/+++++++++++++++++++++++++\\"
            print "", case
            print "-------------------------"
        if fmt == 1:
            print "Case #%d: %s" % (t+1, solution)
        elif fmt == 2:
            print "Case #%d:" % (t+1)
            for i in solution:
                print i
        else:
            print "Case #%d: %s" % (t+1, fmt(solution))
    sys.stderr.write('\n')
main(read_case, solve)
