DEBUG=1

def main():
    T = input()
    for i in range(T):
        N, R, P, S = map(int, raw_input().split())
        print 'Case #%d: %s' % (i+1, ''.join(solve(N, R, P, S)))

def match(a, b):
    if a == b:
        return None
    elif a == 'P':
        if b == 'R':
            return 'P'
        else:
            return 'S'
    elif a == 'R':
        if b == 'S':
            return 'R'
        else:
            return 'P'
    else:
        assert a == 'S'
        if b == 'P':
            return 'S'
        else:
            return 'R'

def reducable(line):
    if len(line) == 1:
        return True
    results = []
    for i in range(len(line)/2):
        tmp = match(line[2*i], line[2*i+1])
        if tmp:
            results.append(tmp)
        else:
            return False
    return reducable(results)

def solve(N, R, P, S):
    hands = ['P', 'R', 'S']    
    h = [None for i in range(2**N)]
    for i_ in range(3**(2**N)):
        # h[0] == i % 3
        # h[1] == (i/3) % 3
        # h[2] == (i/9) % 3
        # h[3] == (i/27) % 3
        for j in range(2**N):
            h[2**N-j-1] = hands[(i_/(3**j)) % 3]
        # print h,
        if h.count('R') != R:
            continue
        if h.count('P') != P:
            continue
        # print
        tmp = reducable(h)
        if tmp:
            return h
    return 'IMPOSSIBLE'
            
main()
