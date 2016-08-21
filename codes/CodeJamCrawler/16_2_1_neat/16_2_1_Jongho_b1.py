import collections

cases = int(raw_input())
for c in xrange(cases):
    letters = collections.Counter(raw_input())
    res = []
    res.append("0"*letters['Z'])
    letters['E']-=letters['Z']
    letters['R']-=letters['Z']
    letters['O']-=letters['Z']
    letters['Z']=0
    res.append("6"*letters['X'])
    letters['I']-=letters['X']
    letters['S']-=letters['X']
    letters['X']=0 
    res.append("8"*letters['G'])
    letters['E']-=letters['G']
    letters['I']-=letters['G']
    letters['H']-=letters['G']
    letters['T']-=letters['G']
    letters['G']=0 
    res.append("7"*letters['S'])
    letters['E']-=letters['S']*2
    letters['V']-=letters['S']
    letters['N']-=letters['S']
    letters['S']=0
    res.append("7"*letters['S'])
    letters['E']-=letters['S']*2
    letters['V']-=letters['S']
    letters['N']-=letters['S']
    letters['S']=0
    res.append("5"*letters['V'])
    letters['F']-=letters['V']
    letters['I']-=letters['V']
    letters['E']-=letters['V']
    letters['V']=0
    res.append("4"*letters['F'])
    letters['O']-=letters['F']
    letters['U']-=letters['F']
    letters['R']-=letters['F']
    letters['F']=0
    res.append("2"*letters['W'])
    letters['T']-=letters['W']
    letters['O']-=letters['W']
    letters['W']=0
    res.append("1"*letters['O'])
    letters['N']-=letters['O']
    letters['E']-=letters['O']
    letters['O']=0
    res.append("9"*letters['I'])
    res.append("3"*letters['R'])
    res.sort()
    print "Case #%d: %s" % (c+1,''.join(res))
