
order = [('Z','ZERO'),('W','TWO'),('X','SIX'),('G','EIGHT'),('H','THREE'),('R','FOUR'),('O','ONE'),('S','SEVEN'),('F','FIVE'),('N','NINE')]

m = {'ZERO':0,'TWO':2,'SIX':6,'EIGHT':8,'THREE':3,'FOUR':4,'ONE':1,'SEVEN':7,'FIVE':5,'NINE':9}

def solve(S):
    digs = { 0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0 }
    for l,d in order:
        while S:
            if l in S:
                for t in d:
                    S = S.replace(t,'',1)
                digs[m[d]] = digs[m[d]] + 1
            else:
                break
    res = ''
    for i in range(10):
        for j in range(digs[i]):
            res += str(i)
    return res


T = int(input())
for t in range(1,T+1):
    S = input()
    print("Case #{}: {}".format(t,solve(S)))
