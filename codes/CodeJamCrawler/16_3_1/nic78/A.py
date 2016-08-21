import fileinput


def stillvalid(sencount):
    m = max(sencount)
    return m<=sum(sencount)-m


def argmax(sencount):
    _max = -1
    _argmax = 0
    for i,el in enumerate(sencount):
        if el > _max:
            _max = el
            _argmax = i

    return (_argmax, _max)

def get_solution(sencount):
    sensum = sum(sencount)
    while sensum>0:
        firstparty, count = argmax(sencount)
        s = '%s' % chr(firstparty+65)
        sensum -=1
        sencount[firstparty] -= 1

        secondparty, count = argmax(sencount)
        sencount[secondparty] -=1
        if stillvalid(sencount):
            sensum-=1
            s += chr(secondparty+65)
        else:
            sencount[secondparty] += 1
        
        print s,
        
    print

    

case = 1
for (linenr, line) in enumerate(fileinput.input()):
    line = line[:-1]
    if fileinput.isfirstline():
        n = int(line)
        continue

    if linenr>n*2:
        print 'too many lines'
        break
    
    if linenr%2==1:
        numparties = int(line)
        continue
    sencount = [int(x) for x in line.split(' ')]
    if len(sencount)!=numparties:
        print len(sencount), numparties
        raise

    
    print 'Case #%d:' % case,
    get_solution(sencount)

    case += 1
    
    
    
    
