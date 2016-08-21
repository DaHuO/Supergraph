def conta(n):
    if n==0:
        return 'INSOMNIA'
    b=False
    i=1
    c = ['0','1','2','3','4','5','6','7','8','9']
    while len(c)!=0:
        n2 = i*n
        #print n2,
        s = str(n2)
        #print c
        for x in s:
            try:
                c.remove(x)
            except:
                pass
        i=i+1
    return n2

f = open("input.in", "r")
fout = open("output.out", "w")
tot = f.readlines()

T = int(tot[0])



for i in range(1,T+1):
    line = tot[i].strip().split(" ")
    number = int(line[0])
    fout.write("Case #{0}: {1}\n".format(i,conta(number)))
    
fout.close()
f.close()

