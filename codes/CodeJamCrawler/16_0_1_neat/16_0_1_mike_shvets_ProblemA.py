import numpy as np

with open('input.txt') as f:
    T = int(next(f))
    Ns = np.zeros(T, dtype='int64')
    for t in range(T):
        Ns[t] = int(next(f))        

with open('output.txt', 'w+') as f:
    for t, N in enumerate(Ns):
        if N == 0:
            f.write('Case #%d: INSOMNIA\n' %(t+1))
        else:
            res = {x: False for x in list('0123456789')}
            cur = 0
            while np.sum(res.values()) < 10:
                cur += N
                for x in list(str(cur)):
                    res[x] = True
            f.write('Case #%d: %d\n' %(t+1, cur))
