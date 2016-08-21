import sys, numpy as np

input = [int(x.strip()) for x in sys.stdin.readlines()][1:]

for case, ip in enumerate(input):
    if ip==0:
        val='INSOMNIA'
    else:
        seen = [False for _ in range(10)]
        i = 1
        while not np.all(seen):
            val = str(ip*i)
            i += 1
            for v in val:
                if not seen[int(v)]:
                    seen[int(v)] = True

    print 'Case #'+str(case+1)+': '+val
