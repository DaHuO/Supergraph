file_in=open("D-small-attempt0.in")
file_out=open("D.out",'w')
cont=file_in.read().splitlines()
T=int(cont[0])
for t in range(1,T+1):
    pl_li=''
    i=int(cont[t].split(' ')[0])
    for pl in range(1,i+1):
        pl_li= pl_li+' '+str(pl)
    file_out.write("Case #"+str(t)+": "+pl_li+"\n")
    print "Case #"+str(t)+": "+pl_li
file_out.close()
file_in.close()
