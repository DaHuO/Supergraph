def solveCase(s):
    ans = 0
    s = s.strip()
    p = None
    for c in s:
        assert(c in '+-')
        if not(p is None) and p != c:
            ans += 1
        p = c
    if s[-1] != '+':
        ans += 1
    return ans
			
with open('B-large.in','r') as fin:
    N = int(fin.readline())
    with open('output.txt','w') as fout:
        for i in range(N):
            c = fin.readline()
            ans = solveCase(c)
            fout.write('Case #')
            fout.write(str(i+1))
            fout.write(': ')
            fout.write(str(ans))
            fout.write('\n')