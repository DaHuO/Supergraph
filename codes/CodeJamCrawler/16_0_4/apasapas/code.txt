def D(K, C, S):
    if C == 1:
        if S < K:
            return 'Impossible'
        else:
            return range(1, K+1)
    elif S < K-1:
        return 'Impossible'
    else:
        return range(2, K+1) if K > 1 else '1'
        