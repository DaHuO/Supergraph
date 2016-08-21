__author__ = 'cary shindell'

inp = open("A-small-attempt0.in", 'r')
opt = open("CS.out", 'w')

N = None
cases = []
for line in inp:
    if N is None:
        N = int(line)
    else:
        cases.append(int(line))

results = []
CTR = 0
for c in cases:
    if c == 0:
        results.append("INSOMNIA")
        CTR += 1
        continue
    if cases.index(c) < CTR:
        results.append(results[cases.index(c)])
        CTR += 1
        continue
    ctr = 1
    result = False
    seen = []
    num = str(c)
    while ctr < 100 and result == False:
        for d in num:
            if d not in seen:
                seen.append(d)
        if len(seen) == 10:
            result = True
            results.append(int(num))
        else:
            num = str(c*ctr)
            ctr += 1
    if result == False:
        results.append("INSOMNIA")
    CTR += 1

Ctr = 1
for x in results:
    opt.write("Case #" + str(Ctr) + ": " + str(x) + "\n")
    Ctr += 1

inp.close()
opt.close()