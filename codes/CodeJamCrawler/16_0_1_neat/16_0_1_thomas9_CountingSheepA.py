'''
Created on 9 Apr 2016

@author: Thomas
'''


num_cases = int(raw_input())

for case in xrange(1, num_cases + 1):

    N = int(raw_input())

    lookup = {}
    for x in xrange(10):
        lookup[str(x)] = False

    x = N
    tries = 0
    limit = 1000000
    while not all(lookup.values()) and tries < limit:
        for number in str(x):
            lookup[number] = True
            
        x += N
        tries += 1

    if tries == limit:
        print "Case #%d: INSOMNIA" % (case)
    else:
        print "Case #%d: %s" % (case, x - N)
        

