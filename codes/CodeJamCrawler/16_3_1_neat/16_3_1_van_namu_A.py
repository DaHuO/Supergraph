import string


party = string.ascii_uppercase

T = int(raw_input())

for case in range(1, T + 1):
    res = ''
    N = int(raw_input())
    P = map(int, raw_input().split())
    document = dict(zip(party[:N], P))

    while any(document.values()):
        sort_p = sorted(document, key=lambda x:document[x], reverse=True)
        p1, p2 = sort_p[:2]
        if document[p1]==document[p2]:
            document[p1] -= 1
            document[p2] -= 1

            m = max(document.values())
            if m > sum(document.values())/2.:
                document[p2] += 1
                res += p1 + ' '
            else:
                res += p1+p2+' '
        elif len([x for x in document if document[x]>0]) > 2:
            document[p1] -= 2
            res += p1 + p1 + ' '
        else:
            document[p1] -= 1
            res += p1 + ' '
    print 'Case #%d: %s' % (case, res)