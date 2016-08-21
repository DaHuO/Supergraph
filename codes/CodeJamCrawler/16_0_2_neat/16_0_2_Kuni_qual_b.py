#coding: utf-8

words = ["+", "-"]

def f(st):
    return len(st[:st.find('-')])

def calc():
    s = raw_input().rstrip()
    count = 0
    while '-' in s:
        idx = s.rfind('-')+1
        v = f(s)
        #print ">>>", v
        if v > 0:
            idx = v
        #print idx, s[:idx]
        target = s[:idx]
        flipped = ""
        for x in target[::-1]:
            if x == "-": flipped += '+'
            elif x=="+": flipped += '-'
            else: break
        s = flipped + s[idx:]
        #print target, ';', flipped, ';', s[idx:]
        #print s
        count += 1

    return count

T = int(raw_input())
for t in xrange(T):
    val = calc()
    print "Case #{}: {}".format(t+1, val)
