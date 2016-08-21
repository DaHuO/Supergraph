fobj_in = open("A-large.in")
fobj_out = open("output.txt","w")
i = 1

for line in fobj_in:
    if i>1:
        a=set()
        for n in range(1,1000002):
            intt=int(line.rstrip())*n
            strr=str(intt)
            a=a.union(set(strr))
            if n<1000001:
                if len(a)==10:
                    fobj_out.write("Case #"+str(i-1) + ": " + str(int(line)*n)+'\n')
                    break
            else:
                  fobj_out.write("Case #"+str(i-1) + ": INSOMNIA"+'\n')
             
    i = i + 1
    if i==1000002:
        break
fobj_in.close()
fobj_out.close()
