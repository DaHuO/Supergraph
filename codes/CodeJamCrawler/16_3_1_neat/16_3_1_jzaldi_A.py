inf = open('input.in','r')
outf = open('output.out','w')

T = int(inf.readline())

def evacuate(P):
    max = 0
    max_ind = 0
    for i in range(len(P)):
        if P[i]>max: 
            max = P[i]
            max_ind = i
    P[max_ind] -= 1
    return str(chr(65+max_ind))

def try_evacuate(P):
    max = 0
    max_ind = 0
    for i in range(len(P)):
        if P[i]>max: 
            max = P[i]
            max_ind = i
    P[max_ind] -= 1
    if is_valid(P) <= 0.5:
        return  str(chr(65+max_ind))
    else:
        P[max_ind] += 1
        return None

def is_valid(P):
    S = sum(P)
    return max(P) /S if S>0 else -1

for t in range(T):
    outf.write('Case #' + str(t+1) + ': ')

    N = int(inf.readline())
    P = [ int(x) for x in inf.readline().split()]
    
    print('Case' + str(t+1))
    while any([x>0 for x in P]):
        c,d = evacuate(P), try_evacuate(P)
        if d is None: outf.write(c+' ') 
        else: outf.write(c+d+' ')
        print(str(P) + ' ' + str(is_valid(P)))
    outf.write('\n')
outf.close()
inf.close()
