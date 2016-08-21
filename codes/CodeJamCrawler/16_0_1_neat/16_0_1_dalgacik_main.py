session = 'A-large'

filename_in = session + '.in'
filename_out = session + '.out'

def solve_case(x):
    if x == 0:
        return "INSOMNIA"
    set_cur = set(str(x))
    x0 = x
    while True:
        if len(set_cur) == 10:
            return x
        x += x0
        set_cur = set_cur.union(set(str(x)))
        

with open(filename_in) as fin, \
    open(filename_out, 'wb') as fout:
    T = int(fin.readline().strip())
    print T
    for i in range(1, T+1):
        x = int(fin.readline())
        y = solve_case(x)
        fout.write('Case #%d: %s\n' %(i, str(y)))


        

