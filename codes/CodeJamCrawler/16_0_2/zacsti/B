IN = open('B.in','r')
OUT = open('B.txt','w')

T = int(IN.readline())
print T
for case in range(1,T+1):
    s = IN.readline()
    c = 0
    flips = 0
    N = len(s)-1
    for i in range(len(s)):
        if s[i]=='+':
            c+=1
    while c<N:
        flips+=1
        if (s[0]=='-'):
            flippoint = 0
            while (s[flippoint]=='-'):
                flippoint+=1
            s = '+'*(flippoint) + s[flippoint:]
        else:
            flippoint = 0
            while (s[flippoint]=='+'):
                flippoint+=1
            s = '-'*(flippoint) + s[flippoint:]
        c = 0
        for i in range(len(s)):
            if s[i]=='+':
                c+=1
    print "Case #" + str(case) + ": " + str(flips)
