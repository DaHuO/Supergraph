def solve(s):
    ans = s[0]
    for l in s[1:]:
        if ord(l) >= ord(ans[0]):
            ans = l + ans
        else:
            ans = ans + l
    return ans


inp = open('A-large.in')
outp = open('Alarge.out', 'w')

T = int(inp.readline())

for i in range(1, T+1):
    S = inp.readline().rstrip()
    ans = solve(S)
    outp.write('Case #{}: {}\n'.format(i, ans))
    print 'Case #{}: {}'.format(i, ans)

inp.close()
outp.close()
