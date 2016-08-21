def flip(s):
    s_flipped = ''
    for c in s[::-1]:
        if c == '+':
            s_flipped += '-'
        else:
            s_flipped += '+'
    return s_flipped


def check(s):
    if '+' not in s:
        return False
    else:
        return True


def arrange(s, flipcount):

    while len(s) > 0:
        i = len(s) - 1

        if s[i] == '+':
            s = s[:i:]

        elif '+' not in s:
        	flipcount+=1
        	break

        else:
            if '+' in s:
                idx = s[::-1].index('+')

                if s[0] == '+':
                    s = flip(s[:(i - idx) + 1:]) + s[(i - idx) + 1::]
                    flipcount += 1
                else:
                    s = flip(s)
                    flipcount += 1
    return flipcount

for t in xrange(input()):
    flipcount = 0
    s = raw_input()
    c=0
    if '-' not in s:
        print 'Case #%d:'%(t+1),flipcount
    elif '+' not in s:
        flipcount += 1
        print 'Case #%d:'%(t+1),flipcount
    else:
        c = arrange(s, flipcount)
    
    	print 'Case #%d:'%(t+1),c
