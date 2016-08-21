def solve(in_file, out_file):
    trials=int(in_file.readline())
    for trial in range(1, trials + 1):
        N = int(in_file.readline())
        if N==0:
            sol = "INSOMNIA"
        else:
            cur = N
            found = dict(zip(str(N), [1]*10))
            while len(found) < 10:
                cur += N       
                for i in str(cur):
                    found[i] = 1
            sol = cur
        out_file.write("Case #{}: {}\n".format(trial, sol))
        
if __name__ == '__main__':
    path='Data/'
    #name='A-sample'
    #name='A-small-attempt0'
    name='A-large'
    raw=open(path+name+'.in', 'r')
    wrt=open(path+name+'.out','w')
    solve(raw, wrt)
    raw.close()
    wrt.close()