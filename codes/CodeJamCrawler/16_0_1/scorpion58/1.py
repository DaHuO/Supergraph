with open('A-large.in') as f:
    lines = f.readlines()
for test in range(int(lines[0])):
    s=set(['0','1','2','3','4','5','6','7','8','9'])
    i=1
    l=int(lines[test+1])
    t=l
    if(t==0):
        print("Case #",test+1,": ",'INSOMNIA',sep='')
    else:
        while(len(s)):
            t=l*i
            i=i+1
            x=list()
            while(t):
                x.append(t%10)
                t=int(t/10)
            x=set([str(u) for u in x])
            s=s.difference(x)
        print("Case #",test+1,": ",l*(i-1),sep='')
