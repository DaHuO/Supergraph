def main():
    f=open('input.txt','r')
    n=int(f.readline())
    testcases=[]
    for i in range(n):
        t=int(f.readline().rstrip('\n'))
        testcases.append(calculate(t))
    fo=open('output.txt','w+')
    for i in range(n):
#        print 'Case #{0}: {1}'.format(i+1,testcases[i])
        fo.write('Case #{0}: {1} \n'.format(i+1,testcases[i]))
#    print testcases

def calculate(t):
    d={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    n=t
    if t==0:
        return 'INSOMNIA'
    count=0
    while True and t<1000000 :
        count=count+1
        t=count*n
#        print t
        for i in range(len(str(t))):
            d[int(str(t)[i])]=d[int(str(t)[i])]+1
#        print d
 #       print check(d)
        if check(d):
#            print 'checked',t
            return t
        else:
            continue;        
    return 'INSOMNIA'
    
def check(d):
    for i in range(10):
        if i==9 and d[i]>0:
            return True
        elif d[i]>0:
            continue;
        elif d[i]==0:
            return False
    
if __name__=="__main__":
    main()
