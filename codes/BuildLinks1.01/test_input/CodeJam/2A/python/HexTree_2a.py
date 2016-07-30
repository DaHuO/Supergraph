def parents(finalists):
    if len(finalists) == 1:
        if finalists[0] == 'R':
            return [['R', 'S'], ['S', 'R']]
        elif finalists[0] == 'S':
            return [['P', 'S'], ['S', 'P']]
        elif finalists[0] == 'P':
            return [['P', 'R'], ['R', 'P']]

    m = len(finalists)
    left = finalists[:m/2]
    right = finalists[m/2:]
    leftparents = parents(left)
    rightparents = parents(right)

    result = []
    for x in leftparents:
        for y in rightparents:
            arr = x + y
            result.append(arr)

    return result


with open("data.txt", 'r') as f:
    with open("data1.txt", 'w') as g:
        T = int(f.readline())
        for i in range(T):
            N, R, P, S = [int(x) for x in f.readline().split()]

            best = None

            for winner in ['P', 'R', 'S']:
                lineup = [[winner]]
                for j in range(N):
                    temp = []
                    for x in lineup:
                        temp += parents(x)
                    lineup = temp

                for x in lineup:
                    Pcount = x.count('P')
                    Rcount = x.count('R')
                    Scount = x.count('S')
                    if Pcount == P and Rcount == R and Scount == S:
                        if best is None or x < best:
                            best = x

            if best is None:
                g.write("Case #%d: %s\n" % ((i + 1), "IMPOSSIBLE"))
            else:
                g.write("Case #%d: %s\n" % ((i + 1), "".join(best)))