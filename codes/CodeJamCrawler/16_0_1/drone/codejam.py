def cot(x):
    d={}
    if x==0:
        return 'INSOMNIA'
    else:
        ctr=1
        las=x
        k=1
        p=x
        while len(d)!=10:

            t=str(x)

            for i in t:
                ger=int(i)
                if ger not in d:
                    d[ger]=ger
                    ctr+=1
                else:
                    d[ger]=1
                    ctr+=1
            k+=1
            x=k*p
            las=(x-p)

        return las

for k in xrange(int(raw_input())):
    t=int(raw_input())
    print 'Case #%s: ' \
          ''%(k+1) + str(cot(t))

