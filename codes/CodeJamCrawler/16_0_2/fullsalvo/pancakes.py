from itertools import groupby

def flip(stack):
    if stack.endswith('+'):
        return (len(stack)-1)
    else:
        return (len(stack))

if __name__ == '__main__':
    T = int(input())
    for zz in range(0,T):
        S = str(raw_input())
        S = ''.join(c for c, _ in groupby(S))
        print "Case #%s: %s" % (zz +1, str(flip(S)))
