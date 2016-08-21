# -*- coding: utf-8 -*-

#file_in = "B-test.in"
#file_out = "B-test.out"
file_in = "B-small-attempt1.in"
file_out = "B-small-attempt1.out"
file_in = "B-large.in"
file_out = "B-large.out"

with open(file_in, "r") as fin, open(file_out, "w") as fout:
    T = int(fin.readline().strip())
    for case in range(1, T + 1):
        N = int(fin.readline().strip())
        w = []
        for i in range(2*N - 1):
            w += [int(x) for x in fin.readline().strip().split()]

        c = {}
        for k in w:
            if k in c:
                c[k] += 1
            else:
                c[k] = 1
        
        s = []
        for k, val in c.items():
            if val % 2 == 1:
                s.append(k)
        
        s.sort()
        fout.write("Case #{0}: {1}\n".format(case, " ".join([str(x) for x in s])))
        print("Case #{0}: {1}".format(case, " ".join([str(x) for x in s])))
print("done")