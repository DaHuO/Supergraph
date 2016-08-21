#Rayun Mehrab - Round 1C Problem A

def maj(s):
    return int(s/2)

def sum_p(p):
    s = 0
    for a in p:
        s = s + a
    return s

def let(n):
    if n == 0:
        return "A"
    if n == 1:
        return "B"
    if n == 2:
        return "C"
    if n == 3:
        return "D"
    if n == 4:
        return "E"
    if n == 5:
        return "F"
    if n == 6:
        return "G"
    if n == 7:
        return "H"
    if n == 8:
        return "I"
    if n == 9:
        return "J"
    if n == 10:
        return "K"
    if n == 11:
        return "L"
    if n == 12:
        return "M"
    if n == 13:
        return "N"
    if n == 14:
        return "O"
    if n == 15:
        return "P"
    if n == 16:
        return "Q"
    if n == 17:
        return "R"
    if n == 18:
        return "S"
    if n == 19:
        return "T"
    if n == 20:
        return "U"
    if n == 21:
        return "V"
    if n == 22:
        return "W"
    if n == 23:
        return "X"
    if n == 24:
        return "Y"
    if n == 25:
        return "Z"

def index_max(n):
    return max(xrange(len(n)),key=n.__getitem__)

def no_maj(p, s):
    for a in xrange(0, len(p)):
        if p[a] > maj(s):
            return (False, a)
    return (True, 0)

t = int(raw_input())

for i in xrange(1, t + 1):
    n = int(raw_input())
    p = [int(s) for s in raw_input().split(" ")]
    s = sum_p(p)
    sln = ""
    while s!=0:
        if s!=1:
            n = index_max(p)
            if p[n] >= 2:
                p[n] = p[n] - 2
                f, g = no_maj(p, s-2)
                if f:
                    sln = sln + let(n) + let(n) + " "
                else:
                    p[n] = p[n] + 1
                    p[g] = p[g] - 1
                    sln =  sln + let(n) + let(g) + " "
                s = s - 2
            else:
                p[n] = p[n] - 1
                f, g = no_maj(p, s-1)
                if f:
                    sln = sln + let(n) + " "
                    s = s - 1
                else:
                    p[g] = p[g] - 1
                    sln = sln + let(n) + let(g) + " "
                    s = s - 2
                
        else:
            n = index_max(p)
            sln = sln + let(n)
            s = s - 1
    
    print "Case #{}: {}".format(i, sln)


exit()
