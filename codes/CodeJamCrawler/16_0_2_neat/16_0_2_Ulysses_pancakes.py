
case = input()

def solve(s):
    parts = list(s)
    previous = '';
    components = 0
    for p in parts:
        if p == previous:
            continue
        else:
            previous = p
            
            components += 1
    if (parts[-1] == '+'):
        components -= 1

    return components;


for i in xrange(1, case+1):
    print 'Case #%d: %s' % (i, solve(raw_input()))
