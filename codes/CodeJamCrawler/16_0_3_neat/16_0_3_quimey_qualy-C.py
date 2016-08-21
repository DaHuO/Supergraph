d = {0:set(['']), 1:set(['0', '1'])}
def generate(k):
    if k not in d:
        d[k] = set([x + '0' for x in generate(k-1)] + [x + '01' for x in generate(k-2)])
    return d[k]

def convert(s, b):
    ans = 0
    p = 1
    for x in s[::-1]:
        if x == '1':
            ans += p
        p *= b
    return ans

T = input()
for t in range(T):
    N, J = map(int, raw_input().split())
    print "Case #%d:" % (t + 1)
    k = 0
    while len(generate(k)) < J:
        k += 1
    for j, f in enumerate(generate(k)):
        if j == J:
            break
        u = '010' + f + '0' * (N - k - 5) + '01'
        v = '10' + f + '0' * (N - k - 5) + '010'
        z = ''.join('1' if u[i] == '1' or v[i] == '1' else '0' for i in range(N))
        print z, ' '.join(str(i) for i in range(3, 12))
        print [convert(z, i) % (i + 1) for i in range(2, 11)]
