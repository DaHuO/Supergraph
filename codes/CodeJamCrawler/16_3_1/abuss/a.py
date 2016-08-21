T = int(raw_input())
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i+n]

for t in range(T):
    N = int(raw_input())
    ps = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', map(int, raw_input().split())))
    ops = dict(ps)
    # print ps
    ep = ''
    while sum(ps.values()):
        cep = ''
        pss = sorted(ps.keys(), key=lambda x: -ps[x])
        cep += pss[0]
        ps[pss[0]] -= 1
        if ps[pss[0]] == 0:
            del ps[pss[0]]
        ep += (cep)
        if not ps:
            break
    ep = list(chunks(ep[::-1], 2))[::-1]
    print "Case #%d:" % (t + 1), ' '.join(ep)
