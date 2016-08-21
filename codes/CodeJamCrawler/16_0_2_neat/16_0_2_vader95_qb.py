def flips(s):
    c = 0
    n = len(s)
    while "-" in s:
        c += 1
        if s[0] == "+":
            rems = s.lstrip("+")
            s = "-"*(n-len(rems)) + rems
            #print s
        else:
            rems = s.lstrip("-")
            s = "+"*(n-len(rems)) + rems
            #print s
    return c
    
t = int(raw_input())
for i in range(t):
    print "Case #{}: {}".format(i+1,flips(raw_input().strip()))
