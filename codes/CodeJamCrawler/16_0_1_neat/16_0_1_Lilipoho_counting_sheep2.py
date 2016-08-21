import sys
def f(path):
    with open(path) as fil:
        lis=fil.readlines()
    out= open("out.txt","a")
    i=1
    for j in range(int(lis[0])):
        dic={}
        num=int(lis[j+1])
        n=0
        if num ==0:
            out.write ("Case #%d: INSOMNIA\n" %(i))
            i+=1
            continue
        while len(dic)<10:
            n+=1
            lst=list(str(n*num))
            for m in lst:
                if m not in dic:
                    dic [m]=1
        if j==int(lis[0])-1:
            out.write( "Case #%d: %d" %(i,n*num))
        else:
            out.write( "Case #%d: %d\n" %(i,n*num))
        i+=1
    out.close()

f(sys.argv[1])
