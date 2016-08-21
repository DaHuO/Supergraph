T=int(input())

for count in range(T):
    S=list(input())
    ans=0
    while S.count('+')!=len(S):
        s_temp=list(S)
        while True:
            if s_temp.pop()!='+': break
        s_temp.append('-')
        if len(s_temp)==1:
            ans+=1
            S[0]='+'
            continue
        if S[0]=='-':
            ans+=1
            s_temp2=[]
            for i in range(0,len(s_temp)):
                if S[i]=='-': s_temp2.append('+')
                else: s_temp2.append('-')
            for i in range(0,len(s_temp2)):
                S[i]=s_temp2[i]
        else:
            c=0
            while c<len(s_temp) and S[c]=='+':
                S[c]='-'
                c+=1
            ans+=1
            s_temp2=[]
            ans+=1
            for i in range(0,len(s_temp)):
                if S[i]=='-': s_temp2.append('+')
                else: s_temp2.append('-')
            for i in range(0,len(s_temp2)):
                S[i]=s_temp2[i]
    print("Case #"+str(count+1)+": "+str(ans))
