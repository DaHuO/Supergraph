def swap(i):
    if i=='+':
        return '-'
    else:
        return '+'
def pancakes():
    s=raw_input().strip()
    s=list(s)
    count=0
    for i in xrange(len(s)-1):
        if s[-(i+1)]=='+':
            if s[-(i+1)]!=s[-(i+2)]:
                for j in xrange(0, len(s) - i-1):
                    s[j] = swap(s[j])
                count+=1
        else:
            count+=1
            for j in xrange(0,len(s)-i):
                s[j]=swap(s[j])
    if s[0]=='-':
        count+=1
        s[0]=swap(s[0])
    #print s
    return count
for i in xrange(int(raw_input().strip())):
    print "Case #%d: %s" % (i + 1, pancakes())
