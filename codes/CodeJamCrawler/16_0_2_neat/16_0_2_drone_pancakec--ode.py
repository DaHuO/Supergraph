def pancake(s):

    a=s.find('-')
    b=s.find('+')
    c=s.count('-')
    ctr=0
    while c!=0 :
        if b==-1:
            ctr+=1
            c=0
        elif s[0]=='-' :
            s='+'*b+s[b:]
            a=s.find('-')
            b=s.find('+')
            ctr+=1
            c=s.count('-')
        else:
            s='-'*a+s[a:]
            b=s.find('+')
            a=s.find('-')
            ctr+=1
            c=s.count('-')
    return ctr



for k in xrange(int(raw_input())):
    t=(raw_input())
    print 'Case #%s: ' \
          ''%(k+1) + str(pancake(t))
