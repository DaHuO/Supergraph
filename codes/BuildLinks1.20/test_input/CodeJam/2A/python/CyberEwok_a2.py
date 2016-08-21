def solve(infile, outfile):
    trials=int(infile.readline())
    transitions = {'R':'SR','P':'PR','S':'PS'}
    for trial in range(1, trials + 1):
        num_rounds, R, P, S = (int(val) for val in infile.readline().strip().split())
        final = gen('P', num_rounds, transitions)
        if (R,P,S) != count(final):
            final = gen('R', num_rounds, transitions)
        if (R,P,S) != count(final):
            final = gen('S', num_rounds, transitions)
        if (R,P,S) != count(final):
            final = "IMPOSSIBLE"
        if final != "IMPOSSIBLE":
            final = sort(final)
        outfile.write("Case #{}: {}\n".format(trial, final))

def sort(word):
    n = 1
    while n < len(word):
        word = sort_sub(word, n)
        n*=2
    return word

def sort_sub(word, num):
    cur = 0
    ret = ""
    while cur < len(word):
        sub1 = word[cur:cur+num]
        cur += num
        sub2 = word[cur:cur+num]
        cur += num
        ret += min(sub1, sub2) + max(sub1, sub2)
    return ret

def gen(initial, num_rounds, trans):
    for i in range(num_rounds):
        tour = ""
        for c in initial:
            tour += trans[c]
        initial = tour
    return initial

def count(tour):
    r,p,s = 0,0,0
    for c in tour:
        if c=='R':
            r += 1
        elif c=='P':
            p+=1
        elif c=='S':
            s+=1
    return r,p,s

if __name__ == '__main__':
    path='Data\\'
    #name='A-sample'
    #name='A-small-attempt1'
    name='A-large'
    infile=open(path+name+'.in', 'r')
    outfile=open(path+name+'.out','w')
    solve(infile, outfile)
    infile.close()
    outfile.close()