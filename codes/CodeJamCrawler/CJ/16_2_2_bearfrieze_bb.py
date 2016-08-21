T = int(input())

def variations(s):
    a = []
    for c in s:
        if c == '?':
            if not len(a):
                a = [str(i) for i in range(10)]
            else:
                tmp = []
                for i in range(10):
                    for o in a:
                        tmp.append(o + str(i))
                a = tmp
        else:
            if not len(a):
                a = [c]
            else:
                a = [o + c for o in a]
    return a

def solve(s):
    a, b = s.split()
    avars = variations(a)
    bvars = variations(b)
    smallest = 1000
    pair = None
    for ao in avars:
        for bo in bvars:
            if abs(int(ao) - int(bo)) <= smallest:
                if abs(int(ao) - int(bo)) == smallest:
                    if int(ao) > int(pair[0]): continue
                    if int(ao) == int(pair[0]) and int(bo) > int(pair[1]): continue
                smallest = abs(int(ao) - int(bo))
                pair = (ao, bo)
    return ' '.join(pair)

for case in range(1, T + 1):
    print('Case #%d: %s' % (case, solve(input())))
