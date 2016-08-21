import math as m

def numdigits(N):
    if (N < 10):
        return 1;
    return numdigits(m.floor(N/10)) + 1;

def digits(N):
    totaln = numdigits(N);
    result = list();
    for i in xrange(totaln):
        base = m.pow(10, i);
        ntop = m.pow(10, i+1);
        forw = m.floor(N/ntop);
        data = int(m.floor((N-forw*ntop)/base));
        if (data not in result):
            result.append(data);
    return result;

def iterate(N, lst, times):
    if (N == 0):
        return "INSOMNIA";
    M = times*N;
    L = digits(M);
    for d in L:
        if d not in lst:
            lst.append(d);
    if (len(lst) == 10):
        return M;
    return iterate(N, lst, times+1);
    
with open('A-large.in') as inFile:
    inp = inFile.readlines();

T = int(inp[0]);
R = 1;
out = open('A-large.out', 'w');
for a in inp[1:]:
    i = int(a);
    print "Case #"+str(R)+": "+str(iterate(i, list(), 1));
    out.write("Case #"+str(R)+": "+str(iterate(i, list(), 1))+"\n");
    R += 1;
out.close();