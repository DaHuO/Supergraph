alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def evac(P,evacsofar,t):
    if t == 0:
        return evacsofar
    if t == 1:
        return evacsofar + ' ' + alph[P.index(1)]
    PL = [ (P[i],i) for i in range(len(P)) ]
    PL.sort(reverse=True)
    m1 = PL[0][1]
    m2 = PL[1][1]
    cand = P
    cand[m1] = cand[m1] - 1
    cand[m2] = cand[m2] - 1
    cmax = max(cand)
    if 2*cmax > t - 2:
        cand[m2] = cand[m2] + 1
        return evac(cand, evacsofar + ' ' + alph[m1], t-1)
    else:
        return evac(cand, evacsofar + ' ' + alph[m1] + alph[m2], t-2)

fi = open('A-large.in','r')
fo = open('out.txt','w')
T = int(fi.readline())
for ii in range(T):
    print('####### Case: ' + str(ii) + '#######')
    N = int(fi.readline())
    P = [int(x) for x in fi.readline().split(' ') if x != '\n']
    nu = evac(P,'',sum(P))
    nu = nu[1:]
    fo.write('Case #'+str(ii+1)+': '+nu+'\n')
fi.close()
fo.close()