__author__ = 'ThomasRiley'


def flip(o, m):
    l = list(o)
    for c in range(0, m+1):
        #print(c)
        if l[c] == '-':

            l[c] = '+'
        else:
            l[c] = '-'


    return "".join(l)

with open('input.txt') as f:
    testCases = f.readlines()
    n = testCases[0]
    for i in range(1, int(n)+1):
        flips = 0
        tc = testCases[i].strip()
        s = len(tc)-1
        while "-" in tc:
            while tc[s] == '+':
                s -= 1
            #print(s)
            tc = flip(tc, s)
            flips += 1

        print("Case #"+str(i)+": "+str(flips))
        """
s = "-+-"
print(flip(s,2))
"""