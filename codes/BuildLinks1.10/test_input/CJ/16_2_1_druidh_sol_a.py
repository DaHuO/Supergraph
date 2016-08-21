#!/usr/bin/python2.7

order = ['Z', 'X', 'S', 'W', 'V', 'F', 'G', 'H', 'O', 'I']
order_num = [0,6,7,2,5,4,8,3,1,9]
delete = {}
delete['Z'] = 'ERO'
delete['X'] = 'SI'
delete['S'] = 'EVEN'
delete['W'] = 'TO'
delete['V'] = 'FIE'
delete['F'] = 'OUR'
delete['G'] = 'EIHT'
delete['H'] = 'TREE'
delete['O'] = 'NE'
delete['I'] = 'NNE'

for case in range(input()):
    s = raw_input()
    s1 = [c for c in s]
    frequency = {}
    for c in list(set(s1)):
        frequency[c] = s1.count(c)
#    print(s)
#    print(frequency)

    sol = []
    for i, initial in enumerate(order):
        if (initial in frequency):
            for j in xrange(frequency[initial]):
                sol.append(order_num[i])
            for c in delete[initial]:
                if (c in frequency):
                    frequency[c] = frequency[c] - frequency[initial]
            del frequency[initial]
#        print initial, frequency

    sol.sort()
#    print(sol)
    print 'Case #%s: %s' % ((case + 1), ''.join(map(str,sol)))
