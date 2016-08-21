from django.template.defaultfilters import first
def get_perfect(ptrn):
    #pattern =  '+++'
    count = 0
    pattern = list(ptrn)

    while ('-' in pattern):
        broke = False
        streak_end = 0
        #print "pattern", pattern
        for streak_end in range(1,len(pattern)):
            #print "pattern[streak_end]", str(pattern[streak_end])
            if pattern[streak_end] != pattern[0]:
                broke = True
                break
        if not broke:
            #print "not broke"
            streak_end += 1 
        #print "streak_end", streak_end   
        
        for i in xrange(0, streak_end):
         #   print "ith pattern", pattern[i]
            if pattern[i] == '+':
                pattern[i] = '-'
            else:
                pattern[i] = '+'
        #print "new pattern", pattern
        count += 1
    return count        

t = int(raw_input())  # number of cases
for i in xrange(1, t + 1):
    pattern = raw_input()            
    print "Case #"+str(i)+": "+str(get_perfect(pattern))