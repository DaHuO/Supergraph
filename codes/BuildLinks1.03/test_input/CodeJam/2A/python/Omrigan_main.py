task = 'A'
type = 2

if type == 0:
    inp = open('sample.in', 'r')
elif type == 1:
    inp = open('%s-small.in' % (task,))
else:
    inp = open('%s-large.in' % (task), )
outp = open('%s.out' % (task,), 'w')

T = int(inp.readline()[:-1])
mat = ['R', 'S', 'P']


def build_tree(top, h):
    if h == 1:
        outp = [mat[top], 0, 0, 0]
        outp[1 + top] += 1
        return outp
    else:
        k = [top, (top + 1) % 3]
        k.sort()
        f = build_tree(k[0], h - 1)
        s = build_tree(k[1], h - 1)
        k = [f[0], s[0]]
        k.sort()
        return [k[0] + k[1], f[1] + s[1], f[2] + s[2], f[3] + s[3]]


for i in range(T):
    c = inp.readline().split()
    N, R, P, S = int(c[0]), int(c[1]), int(c[2]), int(c[3])
    ans = "ZIMPOSSIBLE"
    for j in range(3):
        out = build_tree(j, N+1)
        if out[1]==R and out[2]==S and out[3]==P and out[0]<ans:
            ans = 'Z'+out[0]

    outp.write("Case #%s: %s\n" % (i + 1, ans[1:]))
