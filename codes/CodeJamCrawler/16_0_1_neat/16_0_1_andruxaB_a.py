filename = "/home/andybozhko/Downloads/ipython/codejam/A/A-large"

def stringadd(s1, s2):
    s2 = '0'*(len(s1)-len(s2))+s2
    ss = ''
    c = 0
    for i in range(len(s2)):
        ss = str((int(s1[-i-1])+int(s2[-i-1])+c)%10)+ss
        c = (int(s1[-i-1])+int(s2[-i-1])+c)/10
    if c!=0:
        ss = str(c)+ss
    return ss

fin = open(filename+".in")
fout = open(filename+".out","w")
trials = int(fin.readline())

for T in xrange(trials):
    n = fin.readline().strip()
    num = n
    if num == '0':
        fout.write("Case #{0}: {1}\n".format(T+1,'INSOMNIA'))
    else:
        digits = [str(i) for i in range(10)]
        flag = True
        while flag:
            d = []
            for c in digits:
                if not c in num:
                    d += [c]
            digits = d[:]

            if digits == []:
                flag = False
                break
            num = stringadd(num, n)
        fout.write("Case #{0}: {1}\n".format(T+1,num))
                    
fin.close()
fout.close()