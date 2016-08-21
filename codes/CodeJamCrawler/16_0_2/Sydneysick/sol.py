import re

### RULES
# if S start with 0 then flip the entire stack
# else flip only the repeated 1 continue from begining
def flip(s):
    if (s[0] == '-'):
        s = ''.join('+' if x == '-' else '-' for x in s[::-1])
    else:
        s = re.sub(r'^(\+)+', r'-', s) 
    return s

# remove bottom happy face as no movement is required 
def cleanface(s):
    return re.sub(r'(\+)+$', r'', s) 


t = int(raw_input())
for c in xrange(1, t+1):
    #S = raw_input().replace('+','1').replace('-', '0')
    S = cleanface(raw_input())
    
    fliping = 0
    while (len(S) > 0):
        S = flip(S)
        fliping += 1
        S = cleanface(S)
        
    print "Case #{}: {}".format(c, fliping)
