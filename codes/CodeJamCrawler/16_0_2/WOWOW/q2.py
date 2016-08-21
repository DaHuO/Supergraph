#!/usr/bin/python
#lines = open("input_s.in", 'rt').readlines()
#lines = open("input", 'rt').readlines()
#lines = open("input_small.in", 'rt').readlines()
lines = open("input_large.in", 'rt').readlines()

def flip(s):
#    if (s == "-+"):
#        return [1, "++"]
#    elif (s == "+-"):
#        return [2, "++"]
    res = ""
    for ch in s:
        if ch == '+':
            res = '-' + res
        else:
            res = '+' + res
    return [1, res]


#    print flip(stack)
def run(t, num):
    head = t[0]
    for i in range(1, len(t)):
        if t[i] != head:
            [n, s] = flip(t[:i])
            rs = s + t[i:]
            return [num + n, rs]
    return [num+1, flip(t)]

def check(t):
    for i in t:
        if i == '-':
            return False
    return True

for i in range(1, int(lines[0])+1):
    t = lines[i].strip()
    n = 0
    while not check(t):
    #    print "before", t
        [n, t] = run(t, n)
    print "Case #%d: %d" % (i, n)
