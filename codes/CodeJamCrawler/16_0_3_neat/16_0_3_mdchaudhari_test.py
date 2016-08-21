from math import sqrt
import numpy as np

def factor(n):
    for i in [2,3,5,7,11,13]:
        if not n % i:
            return i
    return 0

with open('input.txt') as f:
    t = int(f.readline())
    for case in range(t):
        params = f.readline()
        n = int(params.split(' ')[0])
        j = int(params.split(' ')[1])

        candidates = set()
        answers = set()

        for i in range(j * 10):
            candidates.add('1' + ''.join(map(lambda x: str(x), np.random.randint(2, size=(n-2,)).tolist())) + '1')

        for c in candidates:
            f = []
            accept = True
            for b in range(2, 11):
                num = int(c, b)
                divisor = factor(num)
                if divisor:
                    f.append(divisor)
                else:
                    accept = False
                    break
            if accept:
                answers.add((c,) + tuple(f))

        print "Case #{0}:".format(t)
        for i in range(j):
            a = answers.pop()
            print ' '.join(map(str, a))