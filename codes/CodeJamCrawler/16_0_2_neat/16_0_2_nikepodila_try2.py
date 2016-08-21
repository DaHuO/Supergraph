# Function for pancake flip
def flipd(ls, pt):
    num = len(ls)
    lstm = list(ls[:pt])
    lstm.reverse()
    ls2 = []
    for k in lstm:
        if k=='+':
            ls2.append('-')
        else:
            ls2.append('+')
    ls2 = ls2 + ls[pt:num]
    return ls2;

# Main part
fi = open('pancake.in', 'r')
T = int(fi.readline().rstrip('\n'))
fo = open('pancake.out','w')
for i in range(1,T+1):
    S = list(fi.readline().rstrip('\n'))
    r = 0
    p = 0
    Snew = list(S)
    tmp = Snew[0]
    for j in S:
        r = r + 1
        if j != tmp:
            Snew = flipd(Snew,r-1)
            tmp = j
            p = p + 1
    if S[-1] == '+':
        fo.write('Case #'+str(i)+': '+str(p)+'\n')
    else:
        fo.write('Case #'+str(i)+': '+str(p+1)+'\n')
fo.close()
fi.close()
