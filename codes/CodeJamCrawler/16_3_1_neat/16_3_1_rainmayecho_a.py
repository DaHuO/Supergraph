import string
import heapq

def g(data):
    parties = [(v, string.ascii_uppercase[i]) for i, v in enumerate(data)]
    s = sum(x[0] for x in parties)
    P = [(-x[0]/float(s), x[0], x[1]) for x in parties]
    heapq.heapify(P)
    r = []
    while parties:
        try:
            b = ''
            ratio, n, letter = heapq.heappop(P)
            s -= 1
            if n > 1:
                heapq.heappush(P, (-(n-1)/float(s), n-1, letter))
            b += letter
            P = [(-x[1]/float(s), x[1], x[2]) for x in P]
            heapq.heapify(P)
            ratio, n, letter = heapq.heappop(P)
            s -= 1
            if n > 1:
                heapq.heappush(P, (-(n-1)/float(s), n-1, letter))
            b += letter
            P = [(-x[1]/float(s), x[1], x[2]) for x in P]
            heapq.heapify(P)
            if b:
                r.append(b)
        except:
            if b:
                r.append(b)
            break
    if len(r[-1]) == 1:
        r[-1], r[-2] = r[-2], r[-1]

    return  ' '.join(r)




h = open('a_out.txt', 'w')
f1 = 'test.txt'
f2 = 'alarge.in'

with open(f2, 'r') as f:
    T = f.readline()
    i = 0
    while i < int(T):
        n = int(f.readline().strip())
        data = [int(e) for e in f.readline().strip().split()]
        r = g(data)
        print 'Case #%s: %s' %(i+1, r)
        h.write('Case #%s: %s\n' %(i+1, r))
        i += 1
