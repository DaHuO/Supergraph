import numpy as np
from collections import Counter

def search(report, ids, rows):
    if not rows:
        return True, ids[0], report
    else:
        row = rows[0]
        for jj in range(len(ids)):
            j = ids[jj]
            if j > 0:
                bad = False
                for r, c in zip(report[j, :], row):
                    if r != c and r != 0:
                        bad = True
                        break
                if not bad:
                    if sum([sum(report[q, :] < row) for q in range(j)]) < j*report.shape[0]:
                        continue
                    report1 = report.copy()
                    report1[j, :] = row
                    vr, rs, rep = search(report1, ids[:jj]+ids[jj+1:], rows[1:])
                    if vr:
                        return vr, rs, rep
            else:
                bad = False
                for r, c in zip(report[:, -j], row):
                    if r != c and r != 0:
                        bad = True
                        break
                if not bad:
                    if sum([sum(report[:, q] < row) for q in range(-j)]) < (-j)*report.shape[0]:
                        continue
                    report1 = report.copy()
                    report1[:, -j] = row
                    vr, rs, rep = search(report1, ids[:jj]+ids[jj+1:], rows[1:])
                    if vr:
                        return vr, rs, rep
        return False, False, None

with open('B-small-attempt3.in') as f:
    with open('b.out', 'w') as out:
        cases = f.readline()
        cases = int(cases)
        for i in xrange(1, cases+1):
            n = int(f.readline())
            rows = [tuple(map(int, f.readline().split())) for j in range(2*n-1)]
            rows.sort()
            report = np.zeros((n, n), dtype=int)
            ids = range(-n+1, n)
            report[0, :] = rows[0]
            ids.sort(key=abs)
            vr, rs, report = search(report, ids, rows[1:])
            if rs <= 0:
                res = ' '.join(map(str, report[:, -rs]))
            else:
                res = ' '.join(map(str, report[rs, :]))
            print 'Case #{i}: {res}'.format(res=res, i=i)
            out.write('Case #{i}: {res}\n'.format(res=res, i=i))