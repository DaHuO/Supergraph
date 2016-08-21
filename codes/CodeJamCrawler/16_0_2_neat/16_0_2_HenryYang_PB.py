import sys
input = file(sys.argv[1])

def solve(v):
    v = list(v[:-1])
    n = 0
    while True:
        if v == ['+']*len(v):
            return n
        m = -100000000
        mi = 0
        for i in range(1, len(v)+1):
            sm = sum(map(lambda x: 1 if x == '-' else 0, v[0:i]))
            if m < sm:
                mi = i
                m = sm
        v_rev = v[0:mi]
        v_rev = map(lambda x: '-' if x == '+' else '+', v_rev)
        v[0:mi] = v_rev
        n += 1

for case in range(int(input.readline())):
    v = input.readline()
    print "Case #%d: %d" % (case+1, solve(v))
