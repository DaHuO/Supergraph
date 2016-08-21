__author__ = 'shiva'
def pancakes(s):
    c = 0
    s = list(s)
    for i in range(len(s)):
        if "-" in s:
            if i == len(s)-1:
                c += 1
                return c
            else:
                if s[i] == s[i+1]:
                    continue
                else:
                    for j in range(i+1):
                        s[j] = "+"
                    c += 1
        else:
            return c

with open("input.in") as ff:
    inp = [lin.rstrip('\n') for lin in ff]

p = 0
o = open("output.txt",'w')
for i in inp[1:]:
    p += 1
    print >>o, "Case #{}: {}".format(p, pancakes(i))
    print "Case #{}: {}".format(p, pancakes(i))
