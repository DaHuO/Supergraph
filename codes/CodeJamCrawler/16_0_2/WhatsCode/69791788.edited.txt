T = int(raw_input())
def solve(n):
    if n%2==0:
        return n-1
    return n

for i in xrange(T):
    string = raw_input()
    ts  = string[0]
    for j  in xrange(1, len(string)):
        if string[j] ==ts[-1]:
            continue
        else:
            ts += string[j]
    l = len(ts) if ts[0] == '-' else len(ts)-1
    if l == 0:
        print "Case #" + str(i+1) + ": " + str(0)
        continue
    b = solve(l)
    if ts[0] == '+':
        b+=1
    print "Case #" + str(i+1) + ": " + str(b)
