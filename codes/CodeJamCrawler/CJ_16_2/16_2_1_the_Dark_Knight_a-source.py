#fi=open("A-small-attempt0.in",'r')#Input File
#fo=open("A-small-attempt0.out",'w')#Output File

fi=open("A-large.in",'r')#Input File
fo=open("A-large.out","w")#Output File

#fi=open("A.in",'r')#Input File
#fo=open("A.out","w")#Output File

digits = ("ZERO", "TWO", "FOUR", "SIX", "EIGHT", "FIVE", "SEVEN", "ONE", "THREE", "NINE")
mp = {"ZERO":"0", "TWO":"2", "FOUR":"4", "SIX":"6", "EIGHT":"8", "FIVE":"5", "SEVEN":"7", "ONE":"1", "THREE":"3", "NINE":"9"}
lst = ['Z', 'W', 'U', 'X', 'G', 'F', 'V', 'O', 'T', 'I']

#("zERO", "TwO", "FOuR", "SIx", "EIgHT", "fIVE", "SEvEN", "oNE", "tHREE", "NiNE")
T = int(fi.readline())
for case in range(1,T+1,1):
    ans = ""
    ############################################
    s = fi.readline().strip()
    for i in range(10):
        if lst[i] in s:
            done = True
            cnt = s.count(lst[i])
            for ch in digits[i]:
                cnt = min(cnt, s.count(ch))
            for ch in digits[i]:
                s = s.replace(ch, '', cnt)
            ans += mp[digits[i]]*cnt    
    ans = "".join(sorted(ans))
    #print ans        
    ############################################
    fo.write("Case #%s: %s\n"%(case, ans))    
