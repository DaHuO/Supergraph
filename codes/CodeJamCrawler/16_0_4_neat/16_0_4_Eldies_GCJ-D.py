from functools import reduce
def prod(l):
    return reduce(lambda x,y:x*y, l, 1)

def solveCase(K,C,S):
    return ' '.join([str(a) for a in list(range(1,K+1))])
    unchecked = list(range(1,K+1))
#    print(K,C,S)
#    if K<C:
#        unchecked = unchecked + [1]*(C-K)
    ans = []
    for i in range(S):
        if len(unchecked)==0:
            break
        shift = (unchecked[0]-1)*(K**(C-1)) 
#        print(K,C,S, "->", ans,shift)
        ans.append(shift + prod(unchecked[1:C]))
        unchecked = unchecked[C:]
    if len(unchecked) > 0:
        return 'IMPOSSIBLE'
    return ' '.join([str(a) for a in ans])

with open('D-small-attempt3.in','r') as fin:
    N = int(fin.readline())
    with open('output.txt','w') as fout:
        for i in range(N):
            K,C,S = fin.readline().split()
            K,C,S = int(K),int(C),int(S)
            ans = solveCase(K,C,S)
            fout.write('Case #')
            fout.write(str(i+1))
            fout.write(': ')
            fout.write(ans)
            fout.write('\n')