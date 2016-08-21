def senate(n):
    n=int(n)
    p=map(int,raw_input().strip().split(' '))
    party={}
    output=[]
    for i in xrange(n):
        party[chr(65+i)]=p[i]
    values=party.values()
    values.sort()
    lasttwo={}
    if values[-1]==values[-2]:
        val2 = party.keys()[party.values().index(values[-2])]
        val2pop=party.pop(val2)
        val1 = party.keys()[party.values().index(values[-1])]
        val1pop=party.pop(val1)
        lasttwo = {val2: val2pop, val1: val1pop}
    while values[-1]!=values[-2] and not lasttwo.keys():
        if values[-1]-values[-2]>1:

            output.append(party.keys()[party.values().index(values[-1])]+party.keys()[party.values().index(values[-1])])
            party[party.keys()[party.values().index(values[-1])]]-=2


        elif values[-1]-values[-2]==1:
            output.append(party.keys()[party.values().index(values[-1])])
            party[party.keys()[party.values().index(values[-1])]] -= 1
            val2 = party.keys()[party.values().index(values[-2])]
            val2pop = party.pop(val2)
            val1 = party.keys()[party.values().index(values[-1]-1)]
            val1pop = party.pop(val1)
            lasttwo = {val2: val2pop, val1: val1pop}
            break
        values = party.values()
        values.sort()
        if values[-1] == values[-2]:
            val2 = party.keys()[party.values().index(values[-2])]
            val2pop = party.pop(val2)
            val1 = party.keys()[party.values().index(values[-1])]
            val1pop = party.pop(val1)
            lasttwo = {val2: val2pop, val1: val1pop}
    for i in party.keys():
        while party[i]:
            if party[i]>1:
                output.append(i+i)
                party[i] -= 2
            elif party[i]==1:
                output.append(i)
                party[i] -= 1
    for i in xrange(max(lasttwo.values())):
        output.append(''.join(lasttwo.keys()))
    return ' '.join(output)
for i in xrange(int(raw_input().strip())):
    print "Case #%d: %s" %(i+1,senate(raw_input().strip()))