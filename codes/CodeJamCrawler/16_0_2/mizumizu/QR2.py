import multiprocessing as mp

def solve(s):
    def flip(c):
        if c == '+': return '-'
        else: return '+'
    n = 0
    while not all(c == '+' for c in s):
        last = s.rfind('-')
        s = ''.join([flip(c) if i <= last else c for i,c in enumerate(s)])
        n += 1
    return n

if __name__ == '__main__':
    pool = mp.Pool(mp.cpu_count())
    
    case_num = int(raw_input())
    results = []
    for i in range(1, case_num+1):
        s = raw_input()
        results.append(pool.apply_async(solve, args=(s,)))
    output = [p.get() for p in results]
    pool.close()
    pool.join()
    for i,out in enumerate(output):
        print 'Case #%d: %s' % (i+1, str(out))
