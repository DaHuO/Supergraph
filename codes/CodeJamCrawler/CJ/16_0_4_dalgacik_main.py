session = 'D-small-attempt0'
#session = 'sample'

filename_in = session + '.in'
filename_out = session + '.out'

    
def solve_case(K, C, S):
    if S < K:
        return 'NOT IMPLEMENTED'
    
    B = K**C
    ls =  range(1, B+1, B/S)
    return ' '.join(map(str, ls))

with open(filename_in) as fin, \
    open(filename_out, 'wb') as fout:
    T = int(fin.readline().strip())
    print T
    for i in range(1, T+1):
        x = fin.readline().strip().split()
        K, C, S = map(int, x)
        
        y = solve_case(K, C, S)
        fout.write('Case #%d: %s\n' %(i, str(y)))
