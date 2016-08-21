import os
os.chdir('/Users/mac/OneDrive/competitions/codejam 2016/round2/grid')

##extra_need
def valid(x, y):
    for i, j in zip(x, y):
        if i >= j:
            return False
    return True

def clean_valid(l):
    if len(l) <= 1:
        return True
    else:
        return valid(l[-2], l[-1])

def clean(ps, n):
    return [(rows, cols) for rows, cols in ps if clean_valid(rows) and clean_valid(cols) and len(rows)<=n and len(cols)<=n]
    
def possibles(s, ps, n):
    if (len(s) == 0):
        return ps
    if (len(ps) == 0):
        ps = [([s[0]], []), ([], [s[0]])]
    else:
        ps = [(list(rows) + [s[0]], list(cols)) for rows, cols in ps] + \
             [(list(rows), list(cols) + [s[0]]) for rows, cols in ps]
    #print ps
    ps = clean(ps, n)
    #print 'clean'
    #print ps
    return possibles(s[1:], ps, n);

def find_rows(s):
    rows = []
    cols = []
    s = sorted(s, key = lambda x: tuple(x))
    for ss in s:
        if len(rows) + len(cols) == len(s)+1:
            break
        if len(rows) == 0:
            rows.append(ss)
            continue
        if valid(rows[-1], ss):
            rows.append(ss)
        else:
            cols.append(ss)
    assert len(rows) == (len(s)+1)/2 or len(cols) == (len(s)+1)/2
    if len(rows) < len(cols):
        return cols, rows
    else:
        return rows, cols

def test(small, large):
    n = len(large[0])
    all = [[x[i] for x in large] for i in range(n)]
    #print all
    for x in small:
        if x not in all:
            return False
    return True


def get_miss(large, small):
    cols_first = set([x[0] for x in small])
    t = 0
    for i, x in enumerate(large[0]):
        if (x not in cols_first):
            t = i
            break
    o = [row[t] for row in large]
    return o
    
    
def getO(s):
    #print s
    s = sorted(s, key = lambda x: tuple(x))
    ps = possibles(s, [], (len(s)+1)/2)
    #print ps
    for rows, cols in ps:
        v = False;
        if (len(cols) < len(rows)):
            v = test(cols, rows)
        else:
            v = test(rows, cols)
        #print v
        if not v:
            continue
        if (len(cols) < len(rows)):
            o = get_miss(rows, cols)
        else:
            o = get_miss(cols, rows)
        print o
        o = [str(x) for x in o]
        o = ' '.join(o)
        return o
        
    


##read test.in
test_f = open('./tests/B-small-attempt3.in.txt')
out_f = open('./tests/B-small-attempt3.out.txt', 'w+')
test_num = None
test_case_num = 1
current_rcs = []
rcs_size = 0
for line in test_f:
    #print line.strip()
    #print rcs_size
    if test_num == None:
        test_num = int(line)
        continue
    if rcs_size == 0:
        rcs_size = int(line)*2-1
        current_rcs = []
        continue
    if rcs_size > 0:
        current_rcs.append([int(x) for x in line.strip().split()])
        rcs_size -= 1
    if rcs_size == 0 and len(current_rcs) != 0:
        T = getO(current_rcs)
        #print '{}, {}, {}'.format(max_s, audiences, extra_need) 
        out_f.write('Case #{}: {}\n'.format(test_case_num, T))
        test_case_num += 1
        
test_f.close()
out_f.close()