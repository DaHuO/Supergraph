#fi=open("A-small-attempt0.in",'r')#Input File
#fo=open("A-small-attempt0.out",'w')#Output File

fi=open("A-large.in",'r')#Input File
fo=open("A-large.out","w")#Output File

#fi=open("A.in",'r')#Input File
#fo=open("A.out","w")#Output File


T = int(fi.readline())
for case in range(1,T+1,1):
    ans = ''
    ############################################
    s =  list(fi.readline().strip())
    ans = s[0]

    for i in range(1, len(s)):
        if s[i] >= ans[0]:
            ans = s[i] + ans
        else:
            ans += s[i]     
    #print ans        
    ############################################
    fo.write("Case #%s: %s\n"%(case, ans))    
