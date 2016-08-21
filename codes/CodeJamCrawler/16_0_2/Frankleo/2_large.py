def shorten(s):
    res = ''
    for i in range(len(s)):
        if i == 0:
            res += s[i]
        else:
            if s[i] != s[i-1]:
                res += s[i]
            else:
                continue
    return res

def ishappy(s):
    if not s:
        return True
    for i in range(len(s)):
        if s[i] != '+':
            return False
    return True


def min_flips(s):
    if ishappy(s):
        return 0

    s = shorten(s)
    if s[-1] == '-':
        return len(s)
    else:
        return len(s)-1


t = int(raw_input())
for i in range(t):
	s = raw_input()
	print 'Case #%d: %d'%(i+1, min_flips(s))