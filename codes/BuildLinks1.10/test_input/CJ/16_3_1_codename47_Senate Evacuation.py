fhr = open("A-large.in",'r')
f = fhr.readline()
T = int(f.strip())
for i in range(1,T+1):
    members = {}
    parties = int(fhr.readline())
    members_raw = (fhr.readline()).split()
    for j in range(0,parties):
        for j1 in range(1,int(members_raw[j])+1):
            try:
                members[j1] = members[j1] + chr(65+j)
            except KeyError:
                members[j1] = chr(65+j)
    l = list(members.keys())
    l.sort()
    l.reverse()
    exit = ""
    for k in range(0,len(l)):
        try:
            times = l[k] - l[k+1]
        except IndexError:
            times = l[k]
        while times>0:
            exit = exit + members[l[k]]
            times += -1
    if (len(exit)%2) != 0:
        answer = exit[0] + " " + ' '.join(exit[i:i+2] for i in range(1,len(exit),2))
    else:
        answer = ' '.join(exit[i:i+2] for i in range(0,len(exit),2))
    print("Case #" + str(i) + ": " + answer)
