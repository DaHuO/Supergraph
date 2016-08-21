def solveForNumber(n):
    s = set()
    if n==0:
        return 'INSOMNIA'
    nn = 0
    while True:
        nn += n
        s.update(str(nn))
        if len(s)==10:
            return nn
			
with open('A-large.in','r') as fin:
    N = int(fin.readline())
    with open('output.txt','w') as fout:
        for i in range(N):
            num = int(fin.readline())
            ans = solveForNumber(num)
            fout.write('Case #')
            fout.write(str(i+1))
            fout.write(': ')
            fout.write(str(ans))
            fout.write('\n')