DEBUG = False

def main():
    T = input()
    for i in range(T):
        S = raw_input()
        print "Case #%d: %s" % (i+1, solve(S))

def search_diff_inds(S):
    prev = S[0]
    i = 0
    inds = []
    for c in S[1:]:
        i += 1
        if prev != c:
            inds.append(i)
        prev = c
    inds.append(len(S))
    return inds


def solve(S0):
    cache = dict()
    cache[S0] = True
    nexts = [S0]
    i = 0
    while True:
        nextnexts = []
        if DEBUG:
            print i, nexts
        for S in nexts:
            if '-' not in S:
                return i
            inds = search_diff_inds(S)
            S_s = [S_ for S_ in [flip(S, ind) for ind in inds] if S_ not in cache]
            for S_ in S_s:
                cache[S_] = True
            nextnexts.extend(S_s)
        i += 1
        nexts = nextnexts

def flip(S, i):
    assert i != 0
    flipped = ''.join(['+' if c == '-' else '-' for c in S[i-1::-1]])
    return flipped + S[i:]

if __name__ == '__main__':
    main()

