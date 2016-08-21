def getdigits(N):
    l=[]
    while(N!=0):
        dig=N%10
        N=N//10
        l.append(dig)
    return(l)

inp_file=open('A-large.in','r')
out_file=open('answer.txt','w')
tesctcase=int(inp_file.readline().strip())
count=1
for t in range(tesctcase):
    i=0
    ans_set={1,2,3,4,5,6,7,8,9,0}
    N=int(inp_file.readline().strip())
    if N==0:
        out_file.write("Case #"+str(count)+": "+"INSOMNIA\n")
        continue
    digs=getdigits(N)
    set_num=set(digs)
    while set_num != ans_set:
        NewN=i*N
        i=i+1
        NewN=getdigits(NewN)
        set_num.update(NewN)
    i=i-1
    count+=1
    out_file.write("Case #"+str(count)+": " +str(N*i)+"\n")
