import sys

def main():
    arr=[]
    x=open("A-large.in", "r")
    for ii in x:
        ii=ii.strip()
        arr.append(ii)
    x.close()

    y=open("A-large.out", "w")
        
    #t=int(sys.stdin.readline())
    t=int(arr[0])
    
    for z in range(1, t+1):
        store={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        #num=int(sys.stdin.readline())
        num=int(arr[z])
        if(num==0):
            y.write("Case #"+str(z)+": INSOMNIA\n")
            print "Case #"+str(z)+": INSOMNIA"
        else:
            check=0
            ctr=1
            while(True):
                num1=num*ctr
                ctr+=1
                string=str(num1)
                for i in string:
                    if store[i]==0:
                        check+=1
                        store[i]=1
                        
                if check==10:
                    y.write("Case #"+str(z)+": "+str(num1)+"\n")
                    print "Case #"+str(z)+": "+str(num1)
                    break
    y.close()
                    
main()
