import random

def flip(pans,i):
    stay=pans[i:]
    inv = [not p for p in pans[0:i]]
#     inv = [not  for
    fin=inv[-1::-1]
    [fin.append(t) for t in stay]
    return fin

def lswitch(pans):
    tpans=[]
    for i in range(len(pans)):
        tpans.append(flip(pans,i))
    lmax=[]
    tmax=[]
    fmax=[]
    for i in range(len(tpans)):
        t=[0]*len(tpans[i])
        f=[0]*len(tpans[i])
        for j in range(len(tpans[i])):
            if tpans[i][j]:
                 t[j] = t[j-1] + 1
                 f[j] = 0
            else:
                t[j] = 0
                f[j] = f[j-1] + 1
        tmax.append(max(t))
        fmax.append(max(f))
        lmax.append(sum([sum(x) for x in zip(t,f)]))
    return len(lmax) - lmax[::-1].index(max(lmax)) - 1

def fliploop(pans):
    i=0
    while not all(pans):
        i=i+1
        if any(pans):
            pans = flip(pans,lswitch(pans))
        else:
            pans=flip(pans,len(pans))
    return i

def conv(pm):
    boo=[False]*len(pm)
    for i in range(len(pm)):
        if pm[i]=='+':
            boo[i]=True
    return boo

    filename='ProbB-test'
file_in = open(filename+'.in','r')
file_out = open(filename+'.out','w')
num_sets=int(file_in.readline())
for i in range(num_sets):
    pans = conv(file_in.readline().rstrip('\n'))
#     print file_in.readline()
#     print pans
    num_flips = fliploop(pans)
    print num_flips
    file_out.writelines('Case #%s: %d\n'%(i+1,num_flips))

file_in.close()
file_out.close()
