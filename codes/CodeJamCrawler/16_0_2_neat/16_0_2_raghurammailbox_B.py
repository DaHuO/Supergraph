file_in=open("B-large.in")
file_out=open("B-large.out",'w')
cont=file_in.read().splitlines()
T=int(cont[0])
for t in range(1,T+1):
    i=cont[t]
    cur=i[0]
    change=0
    for l in list(i):
        if(cur!=l):
            change=change+1
            cur=l
    if i[-1]=='-':
         change=change+1
        
    file_out.write("Case #"+str(t)+": "+str(change)+"\n")
    print "Case #"+str(t)+": "+str(change)+"\n"
file_out.close()
file_in.close()
