#fi=open("A-small-attempt0.in",'r')#Input File
#fo=open("A-small-attempt0.out",'w')#Output File

fi=open("A-large.in",'r')#Input File
fo=open("A-large.out","w")#Output File

#fi=open("A.in",'r')#Input File
#fo=open("A.out","w")#Output File


T = int(fi.readline())
for case in range(1,T+1,1):
    ans = 'INSOMNIA'
    mp = set()
    ############################################
    n =  int(fi.readline())
    ind = 1

    if n != 0:
        while len(mp) != 10:
            ans = n * ind
            st = str(ans)
            mp = mp.union(list(st))
            ind += 1

    #print ans        
    ############################################
    fo.write("Case #%s: %s\n"%(case, ans))    
