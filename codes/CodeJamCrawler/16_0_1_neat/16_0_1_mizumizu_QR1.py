import multiprocessing as mp

def solve(N):
    if N == 0: return 'INSOMNIA'
    digit = set()
    n = 0
    while len(digit)<10:
        n += N
        digit.update(set(list(str(n))))
    return n

if __name__ == '__main__':
    pool = mp.Pool(mp.cpu_count())
    
    case_num = int(raw_input())
    results = []
    for i in range(1, case_num+1):
        N = int(raw_input())
        results.append(pool.apply_async(solve, args=(N,)))
    output = [p.get() for p in results]
    pool.close()
    pool.join()
    for i,out in enumerate(output):
        print 'Case #%d: %s' % (i+1, str(out))
