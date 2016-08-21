in1 = open('mtx.in')
out1 = open('mtx.out', 'w')


T = int(in1.readline())

for i in range(0, T):
    n = int(in1.readline())
    m = [0]*2501
    for j in range(0,2*n-1):
        q = [int(ii) for ii in in1.readline().split()]
        #print q
        for k in range(0,len(q)):
            if m[q[k]] == 1:
                m[q[k]] = 0
            else:
                m[q[k]] = 1

    out1.write("Case #%d:" %(i+1))
    for j in range(0,2501):
        if m[j] == 1:
            out1.write(" %d" %j)
    out1.write('\n')
    
in1.close();
out1.close();