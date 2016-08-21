
data = open("B-large.in").read().split()
n = int(data[0])
data = data[1:]
answ = []

def flip(s, r):
    fh = s[:r][::-1]
    nh = ""
    for c in fh:
        nh += '+' if c=='-' else '-'
    return nh + s[r:]

for p in data:
    ctr = 0
    while p != '':
        for i in xrange(len(p)-1, -1, -1):
            if p[i] == '-':
                k = i+1
                break
            elif i == 0:
                k = 0
        p = p[:k]
        if p == '':
            break

        for i,c in enumerate(p):
            if c == '+':
                k = i
                break
            elif i == len(p)-1:
                k = len(p)
        
        if k == 0:
            for i,c in enumerate(p):
                if c=='-':
                    k = i
                    break
        p = flip(p, k)
        
        ctr += 1
    answ.append(ctr)

with open("B-large.out", 'w') as f:
    for i,o in enumerate(answ):
        f.write("Case #{}: {}\n".format(i+1, o))

#print answ[:20]
