import sys
import string

# Arguments: [in] [out]
# Defaults: in='input.txt', out=stdout

def order(xs):
    x = max(xs)
    c = next(i for i in xrange(len(xs)) if xs[i] == x)
    m = []
    h = xs[:c]
    t = xs[c:]
    while x in t:
        t.remove(x)
        m.append(x)
    if c == 0: return m + t
    return m + order(h) + t

if len(sys.argv) > 1:
    input_file = len(sys.argv)>1 and sys.argv[1] or 'input.txt'
    outf = len(sys.argv)>2 and open(sys.argv[2],'w') or sys.stdout
    with open(input_file) as f:
        T = int(f.readline())
        for x in range(T):
            ws = list(f.readline().strip())
            outf.write('Case #{0}: '.format(x+1))
            W = order(ws)
            outf.write(''.join(W))
            outf.write('\n')
