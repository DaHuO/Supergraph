"""
    Author : NILESH AGARWAL
    Gmail : nilesh.kumpawat@gmail.com
"""

def find_list(y):
    o = list(y.items())
    g = []
    for s,j in o:
        if j%2 is not 0:
            g.append(int(s))
    g = sorted(g)
    return g


cases=0
filer = open('ib2.in')
filew = open('pob2.txt','w')
matrix = filer.read()
matrix = [item.split() for item in matrix.split('\n')[:-1]]
i = []
for u in matrix:
    i.extend(u)
cnt = 0
t = int(i[cnt])
cnt=cnt+1
for q in range(t):
    l = int(i[cnt])
    cnt=cnt+1
    cases = cases+1
    filew.write("Case #"+str(cases)+":"+" ")
    r = {}
    inputs = 2*(l**2)-l
    for w in range(inputs):
        ele = i[cnt]
        cnt=cnt+1
        if r.has_key(ele):
            r[ele]= r[ele] + 1
        else:
            r[ele] = 1
    new_list = find_list(r)
    for q in new_list:
        filew.write(str(q)+" ")
    filew.write("\n")
filew.close()
filer.close()
