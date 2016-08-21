fr = open('input2.in','r')
t = int(fr.readline())
check=range(0,10)
multiply=range(1,101)
case=0
fw = open('output2.txt','w')
while(t):
    t=t-1
    rem=range(0,10)
    N=int(fr.readline())
    cnt=0
    for num in multiply:
        nu=N*num
        string= list(set(str(nu)))
        for y in check:
            if str(y) in string and y in rem:
                rem.remove(y)
                cnt=cnt+1
                if cnt is 10:
                    case=case+1
                    fw.write('Case #'+str(case)+": "+str(nu)+'\n')
                    break
        if cnt is 10:
            break
    if cnt is not 10:
        case=case+1
        fw.write('Case #'+str(case)+": "+"INSOMNIA\n")
fw.close()
fr.close()
                                 
                
            
    
