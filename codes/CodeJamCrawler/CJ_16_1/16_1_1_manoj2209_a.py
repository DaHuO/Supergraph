def fa(l):
    a=l[0]
    str=''
    str+=a
    for li in l[1:]:
        if ord(li) < ord(str[0]):
            str=str+li
        else:
            str=li+str
    return str

t=int(raw_input())
for x in xrange(1,t+1):
    l=raw_input()
    print 'Case #{}: {}'.format(x,fa(l))