test_case=int(raw_input())
inputs=[]
for i in range(test_case):
    val=int(raw_input())
    inputs.append(val)

for a in inputs:
    if a==0:
        print 'Case #%s' %str(inputs.index(a)+1)+': INSOMNIA'
    else:
        i=1
        sat=set()
        while(True):
            top=i*a
            sat=sat.union(set(str(top)))
            if len(sat)==10:
                break
            else:
                i=i+1
        print 'Case #%s' %str(inputs.index(a)+1)+': %s' %top
    
