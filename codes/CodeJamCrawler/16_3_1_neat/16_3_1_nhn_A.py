import sys
from time import time as ti

def A(ini,out):
    f = open(ini,'r')
    o = open(out,'w')
    T = int(f.readline())
    for t in range(T):
        N = int(f.readline())
        sens = [int(x) for x in f.readline().split(' ')]
        tot = sum(sens)
        plan = []
        while sum(sens)>0:
            cop = sens[:]
            if (sum(cop)==3) and (len(cop)==3):
                a = cop.index(max(cop))
                plan.append(chr(65+a))
                sens[a]-=1
                continue
            a = cop.index(max(cop))
            cop.remove(cop[a])
            b = cop.index(max(cop))
            if b>=a:
                b+=1
            plan.append(''.join([chr(65+a),chr(65+b)]))
            sens[a]-=1
            sens[b]-=1
        o.write("Case #"+str(t+1)+": "+" ".join(plan)+"\n")
        print("Case #"+str(t+1)+": "+" ".join(plan)+"\n")

def main(argv):
    ini = "A-small-attempt0.in"
    out = "A-small-attempt0.txt"
    start = ti()
    A(ini,out)
    end = ti()
    print (end-start)

if (__name__ == "__main__"):
    main(sys.argv[1:])

