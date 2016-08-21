import permutation


T = int(raw_input())

def get_tie_prob(P):
    K = len(P)
    half_K = K/2
    all_comb = permutation.get_combination(half_K, [x for x in xrange(0,K)])
    result_prob = 0
    all_index_set = set([x for x in xrange(0,K)])
    for comb in all_comb:
        index_set = set(comb)
        complement_index_set = all_index_set - index_set
        cur_P = 1
        for i in index_set:
            cur_P *= P[i]
        for i in complement_index_set:
            cur_P *= (1-P[i])
        result_prob += cur_P
    return result_prob

#print(get_tie_prob([0.3,0.8]))


for t in xrange(1, T+1):
    N, K = tuple([int(x) for x in raw_input().strip().split()])
    P = [float(x) for x in raw_input().strip().split()]
    P.sort()

    all_P_choices = permutation.get_combination(K, P)
    max_tie_prob = 0.
    for P_choices in all_P_choices:
        #print(P_choices)
        tie_prob = get_tie_prob(P_choices)
        #print(tie_prob)
        if tie_prob > max_tie_prob:
            max_tie_prob = tie_prob
            #print("CHANGE MAX_TIE")
    print("Case #%d: %f" %(t, max_tie_prob))

