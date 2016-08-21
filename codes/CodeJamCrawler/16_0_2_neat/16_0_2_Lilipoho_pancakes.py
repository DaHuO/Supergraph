import sys
def f(path):
    with open(path) as fil:
             lis=fil.readlines()
    out= open("out.txt","a")
    i=0
    for j in range(int(lis[0])):
        i+=1
        lst=list(lis[j+1])
        lst[-1]='+'
        n=0
        for m in range(len(lst)-1):
            if lst[m]!=lst[m+1]:
                n+=1
        if j==int(lis[0]):
                    out.write('Case #%d: %d' %(i,n))
        else:
            out.write('Case #%d: %d\n' %(i,n))
    out.close()

f(sys.argv[1])
