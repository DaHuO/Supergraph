def proc(a):
    if a==0:
        return('INSOMNIA')
    j=0
    c=0
    ea=[0,1,2,3,4,5,6,7,8,9]
    ga=[]
    while(set(ea)!=set(ga)):
        j+=1
        for i in str(a*j):
            ga.append(int(i))
        
    return(a*j)




def main(infile,outfile):
    f=open(str(infile),'r+')
    n=int(f.readline())
    o=open(str(outfile),'w+')
    for i in range(1,n+1):
        dig=int(f.readline())
        ans=proc(dig)
        o.write('Case #{}: {}\n'.format(i,ans))
    f.close()
    o.close()


