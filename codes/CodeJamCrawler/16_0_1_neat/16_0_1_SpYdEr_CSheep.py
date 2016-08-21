def CountSheep():
    infile=open('A-large.in')
    outfile=open('A-large.out','w')
    T=int(infile.readline())
    for x in range(T):
        lst=[]
        iN=''
        b=0
        N=int(infile.readline())
        if(N==0):
            s2='INSOMNIA'
        else:
            i=1
            while(i<=500):
                iN=str(i*N)
                for a in iN:
                    lst=lst+[int(a)]
                b=checkList(lst)
                if b==10:
                    s2=iN
                    break
                i+=1
            if(b!=10):
                s2='INSOMNIA'
        s1='Case #'+str(x+1)+': '+s2+'\n'
        outfile.write(s1)
        print(s1[:len(s1)-1])
    infile.close()
    outfile.close()
    return

def checkList(lst):
    found=0
    n=0
    i=0
    if len(lst)==0:
        return found
    else:
        while(i<len(lst)):
            if (lst[i]==n):
                found+=1
                n+=1
                i=0
                if n==10:
                    break
            else:
                i+=1
    return found


#Function Call:-
print(CountSheep())
