def getsteps(new_pattern):
    type1 = 0
    type2 = 0
    if new_pattern[0]=='-' and new_pattern[-1]=='-':
        type1=1
        invert=True
    elif new_pattern[0]=='+'and new_pattern[-1]=='+':
        type1=0
        invert=False
    elif new_pattern[0]=='-'and new_pattern[-1]=='+':
        type1=1
        invert=False
    elif new_pattern[0]=='+'and new_pattern[-1]=='-':
        type1=2
        invert=True
    for i in range(1,len(new_pattern)-1):
        if(new_pattern[i]=='-' and not invert):
            type2=type2+1
        elif(new_pattern[i]=='+' and invert):
            type2=type2+1
    type2=type2*2
    return type1+type2
        
T=int(input())
for t in range(1,T+1):
    pattern=raw_input()
    pattern=str(pattern)
    if len(pattern) is 0:
        print "Case #"+str(t)+": "+str(0)
    else:
        new_pattern=pattern[-1]    
        for i in range(len(pattern)-1,-1,-1):
            if pattern[i]==new_pattern[0]:
                pass
            else:
                new_pattern= pattern[i]+new_pattern
        print "Case #"+str(t)+": "+str(getsteps(new_pattern))
