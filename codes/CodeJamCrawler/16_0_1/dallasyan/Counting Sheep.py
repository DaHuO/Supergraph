with open("inp.txt") as f:
    with open("out.txt","w+") as g:
        i=0
        for line in f:
            j=0
            k=0
            l=[0,0,0,0,0,0,0,0,0,0]
            n=0
            if i==0:
                lines=int(line)
            else:
                if int(line)==0:
                    g.write("Case #"+str(i)+": INSOMNIA\n")
                    print("Case #"+str(i)+": INSOMNIA")
                else:
                    while k<10:
                        n+=1
                        linez=str(n*int(line))
                        for m in linez:
                            if l[int(m)]==0:
                                k+=1
                                l[int(m)]=1
                    g.write("Case #"+str(i)+": "+linez+"\n")
                    print("Case #"+str(i)+": "+linez)
            i+=1
        
