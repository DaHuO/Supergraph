t=int(raw_input())
ss=[''];
ts="";
for i in range(t):
    s=raw_input();
    for j in s:
        if(j>=ss[0]):
            ss.insert(0,j);
        elif(j<ss[0]):
            ss.append(j);
    print "Case #"+str(i+1)+': '+''.join(ss);
    ts="";
    ss=[''];
