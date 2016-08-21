q = lambda (a,(b,c)): b if a==c else c

def f(a, X):
    if type(X) == int: return X
    else: return q((a,X))

def rankandfile(data):
    symmetry = True
    rows = []
    N = len(data[0])
    for x in range(N):
        shortest = min([el[x] for el in data])
        candidates = []
        for i in range(len(data)-1, -1, -1):
            if data[i][x] == shortest:
                candidates.append(data.pop(i))
        if len(candidates) == 1:
            rows.append(candidates[0])
            wincol = x
        else: rows.append(zip(*candidates))
    return [f(a, X) for a,X in zip(rows[wincol], zip(*rows)[wincol])]

def main():
    cases = int(raw_input())
    for case in range(1, cases+1):
        N = int(raw_input())
        data = []
        for i in range(2*N-1):
            data.append(map(int, raw_input().split()))
        print "Case #%i:" %case, ' '.join(map(str, rankandfile(data)))

if __name__ == '__main__':
    main()

