from itertools import combinations

T = input()

def p_outcome(P, K, i, yes, no):
    if i == K:
        if yes == 0 and no == 0:
            return 1.0
        else:
            return 0.0

    prob_of_tie_given_yes = P[i] * p_outcome(P, K, i+1, yes-1, no)
    prob_of_tie_given_no = (1 - P[i]) * p_outcome(P, K, i+1, yes, no-1)

    return prob_of_tie_given_yes + prob_of_tie_given_no

for case_num in xrange(T):
    N, K = map(int, raw_input().split())
    P = map(float, raw_input().split())

    ans = 0.0

    for selection in combinations(P, K):
        ans = max(ans, p_outcome(selection, K, 0, K/2, K/2))

    print 'Case #%d: %s' % (case_num + 1, ans)
