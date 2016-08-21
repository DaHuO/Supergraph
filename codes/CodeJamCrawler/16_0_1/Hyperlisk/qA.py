
import fileinput

inp = fileinput.input()
def _(*to):
    global inp
    line = inp.readline()
    if len(to) == 0:
        return line
    elif len(to) > 1:
        return map(lambda x: x[0](x[1]), zip(to, line.split()))
    elif type(to[0]) is list:
        return map(to[0][0], line.split())
    elif to[0] is set:
        return set(line.split())
    else:
        return to[0](line)

T = _(int)
for i in range(T):
    i = i + 1
    N = _(int)
    
    if N == 0:
        print "Case #%s: INSOMNIA" % (i,)
        continue
    
    s = set()
    NN = N
    while len(s) < 10:
        for c in str(NN):
            s.add(c)
        NN += N
    
    print "Case #%s: %s" % (i, NN - N)

