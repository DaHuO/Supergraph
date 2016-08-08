_map = {
    'R': 'RS',
    'S': 'PS',
    'P': 'PR'
}
def solve(N, R, P, S):
    """ solve the problem """

    for win in ['R', 'P', 'S']:
        s = win 
        for i in range(N):
            next_s = ''
            for c in s:
                next_s += _map[c]
            s = next_s
        _R = 0
        _P = 0
        _S = 0
        for c in s:
            if c == 'R': _R += 1
            if c == 'P': _P += 1
            if c == 'S': _S += 1
        if R == _R and P == _P and S == _S: 
            for i in range(N):
                next_s = ''
                cur = 0
                interval = 2**i
                while cur < 2**N:
                    left = s[cur:cur+interval]
                    right = s[cur+interval:cur+interval*2]
                    if left < right:
                        next_s += left + right
                    else:
                        next_s += right + left
                    cur += 2 * interval
                s = next_s

            return s 

    return 'IMPOSSIBLE'


def parse():
    """ parse input """

    N, R, P, S = [int(x) for x in input().split()]

    return N, R, P, S


def main():
    
    T = int(input())

    # solve
    for t in range(1, T+1):
        params = parse()
        result = solve(*params)
        print('Case #%d: %s' % (t, result))


if __name__ == '__main__':

    main()
