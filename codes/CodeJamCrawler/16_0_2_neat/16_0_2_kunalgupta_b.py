t = int(raw_input())
for _ in xrange(t):
    s = raw_input()
    if len((set(list(s))))==1:
        if s[0] == '+':
            print "Case #" + str(_+1) + ": 0"
        else:
            print "Case #" + str(_+1) + ": 1"
        continue
    cnt=0
    for i in xrange(len(s)-1):
        if(s[i]+s[i+1] in ["+-", "-+"]):
            cnt+=1
    if s[0] == '-':
        if cnt%2==0:
            cnt+=1
    else:
        if cnt%2==1:
            cnt+=1
    print "Case #" + str(_+1) + ": " + str(cnt)
