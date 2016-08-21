import sys

def y():
    for l in sys.stdin:
        yield from l.split()
x = y()

T = int(next(x))

max = 0
def Try(N, K, pos, n, k, vec):
    global max
    if k == K:
        if vec[K>>1] > max:
            max = vec[K>>1]
            return
    if n == N:
        return

    Try(N, K, pos, n+1, k, list(vec))
    for t in reversed(range(K>>1)):
        vec[t+1] = vec[t] * pos[n] + vec[t+1] * (1-pos[n])
    vec[0] *= (1-pos[n])
    Try(N, K, pos, n+1, k+1, vec)


for i in range(T):
    N = int(next(x))
    K = int(next(x))
    sys.stdout.write("Case #%s: " % (i+1))

    max = 0
    pos = []

    for j in range(N):
        pos.append(float(next(x)))

    vec = [0] * ((K>>1)+1)
    vec[0] = 1
    Try(N,K,pos,0,0,vec)
    sys.stdout.write(str(max)+"\n")



