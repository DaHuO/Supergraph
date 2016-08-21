def readint(fin): return int(fin.readline())
def readarray(fin, t): return map(t, fin.readline().strip().split())

in_file, out_file = 'B-large.in', 'B-large.out'

with open(in_file, 'r') as fin, open(out_file, 'w') as fout:
    T = int(fin.readline().strip())
    for _t in range(1, T+1):
        str = fin.readline().strip()
        n = len(str)
        res = 0

        i = n - 1
        while i >= 0 and str[i] == '+':
            i -= 1

        if i < 0:
            fout.write('Case #%d: %d\n' % (_t, 0))
        else:
            cnt = 0
            for j in range(i):
                if str[j] != str[j + 1]:
                    cnt += 1
            fout.write('Case #%d: %d\n' % (_t, cnt+1))
