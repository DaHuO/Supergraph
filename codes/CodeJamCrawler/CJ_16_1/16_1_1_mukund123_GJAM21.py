tc=int(raw_input())
for i in range(tc):
    inp=raw_input()
    s=""+inp[0]  
    for k in range(1,len(inp)):
        if inp[k]>=s[0]:
            s=inp[k]+s[0::]
        else:
            s=s[0::]+inp[k]
    print "Case #" + str(i+1)+":"+" "+ s
