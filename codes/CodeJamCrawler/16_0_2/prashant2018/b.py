t = int(raw_input())
k=1

def flip(s1):
    s1 = list(s1)
    for i in range(len(s1)):
        if s1[i] == '-':
            s1[i] = '+'
        else:
            s1[i] = '-'
    #print str(s1)
    return ''.join(s1)


while t:
    s = str(raw_input())
    f=0
    count = 0
    while True:
        #s = list(s)
        #print s
        for i in range(len(s)):
            if '-' not in s:
                print "Case #"+str(k)+": "+str(count)
                f=1
                break
            else:
                if s[-1] == '+':
                    s = s[:-1]
                    #print s
                else:
                    s = flip(s)
                    #print s
                    count = count + 1
        if f==1:
            break
    t=t-1
    k=k+1
