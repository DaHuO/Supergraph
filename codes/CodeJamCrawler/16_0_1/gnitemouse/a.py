import fileinput
from sys import maxint

t = int(raw_input())
for case in range(t):
    insomnia = True
    digits = set()
    n = int(raw_input())
    num = n;
    # while num < maxint-n:
    for c in range(1000000):
        for x in list(str(num)):
            digits.add(int(x))
        if len(digits) == 10:
            insomnia = False
            break
        num = num+n
    if insomnia:
        print 'Case #{}: {}'.format(case+1, 'INSOMNIA');
    else:
        print 'Case #{}: {}'.format(case+1, num);
