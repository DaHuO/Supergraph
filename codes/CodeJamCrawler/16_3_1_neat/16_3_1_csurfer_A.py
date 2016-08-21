from collections import defaultdict


def solve():
    chars = int(input())
    al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    freq = defaultdict(lambda: 0)
    arr = map(int, raw_input().split())
    sm = 0
    for i in xrange(chars):
        freq[al[i]] = arr[i]
        sm += arr[i]
    result = []
    while sm > 3:
        mxFreq = max(freq.values())
        myKey = ''
        for key in freq.keys():
            if freq[key] == mxFreq:
                myKey += key
                freq[key] -= 1
            if len(myKey) == 2:
                break
        result.append(myKey)
        sm -= len(myKey)
    if sm == 3:
        key1 = None
        key2 = None
        for key in freq.keys():
            if freq[key] == 1 and key1 == None:
                key1 = key
            elif key2 == None:
                key2 = key
            else:
                key2 += key
        result.append(key1)
        result.append(key2)
    if sm == 2:
        myKey = ''
        for key in freq.keys():
            if freq[key] == 1:
                myKey += key
                freq[key] -= 1
            if len(myKey) == 2:
                break
        result.append(myKey)
    return ' '.join(result)

tc = int(input())
TC = int(tc)
while tc > 0:
    tc -= 1
    ans = solve()
    print 'Case #{}: {}'.format(TC - tc, ans)
