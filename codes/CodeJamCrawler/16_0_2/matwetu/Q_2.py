flip = lambda x:1-x

def move(pk, n):
    return map(flip, pk[:n][::-1]) + pk[n:]

def addpk(s, pk):
    s.add(''.join(map(str, pk)))

def existpk(s, pk):
    return ''.join(map(str,pk)) in s

def solve_stupid(pk):
    moves = [[pk]]
    smoves = set()
    addpk(smoves, moves[0][0])
    target = '1' * len(pk)
    while 1:
        cur = moves[-1]
        if not cur : return
        moves.append([])
        for tpk in cur:
            if ''.join(map(str, tpk)) == target:
                return len(moves) - 2
            for n in range(1, len(pk)+1):
                npk = move(tpk, n)
                if not existpk(smoves, npk):
                    addpk(smoves, npk)
                    moves[-1].append(npk)

def solve(pk):
    #expected = solve_stupid(pk)
    if len(pk) == 0:
        return 0
    last = len(pk) - 1
    while last >= 0 and pk[last] == pk[-1]: last -= 1
    if pk[-1] == 1:
        return solve(pk[:last+1])
    else:
        return solve(map(flip, pk[:last+1])) + 1

tot = int(raw_input())
dic = {'-':0,'+':1}
for caseidx in range(1, tot + 1):
    pk = map(lambda x:dic[x], raw_input().strip())
    print "Case #%d: %s" % (caseidx, solve(pk))