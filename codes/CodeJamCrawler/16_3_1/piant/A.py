from collections import Counter

def go(s):
    res = []
    cnt = Counter({chr(ord('A') + i): e for i, e in enumerate(s)})
    # print cnt
    while sum(cnt.values()):
        com = cnt.most_common()
        i = 0
        # print 'com', com
        while i < len(com) and com[i][1] == com[0][1]:
            i += 1
        if len(com) == 3 and i == 2:
            res.append(com[0][0])
            cnt[com[0][0]] -= 1
            # if i == 1:

        elif i % 2 == 0:
            res.append(com[0][0] + com[1][0])
            cnt[com[0][0]] -= 1
            cnt[com[1][0]] -= 1
        else:
            res.append(com[0][0])
            cnt[com[0][0]] -= 1
        for k, v in cnt.items():
            if v == 0:
                del cnt[k]
    return res

cases = [[2,2],[3,2,2],[1,1,2],[2,3,1]]

# for i, case in enumerate(cases):
n = int(raw_input())
for i in range(n):
    input()
    case = map(int, raw_input().strip().split())
    print "Case #%d: %s" % (i+1, ' '.join(go(case)))
