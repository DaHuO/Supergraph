#Rayun Mehrab - Qualification Problem B Large

t = int(raw_input())
    
def check_plus():
    for i in l:
        if i != '+':
            return False
    return True

def flip(i):
    if l[i] == '+':
        l[i] = '-'
    else:
        l[i] = '+'
    return

for i in xrange(1, t + 1):
    n = raw_input()
    l = []
    a = 0
    for m in xrange(0, len(n)):
        l.append(n[m])

    while not check_plus():
        c = 0
        flip(0)
        while c+1<len(l) and l[c+1] != l[c]:
            flip(c+1)
            c = c + 1
        a = a + 1
            
    print "Case #{}: {}".format(i, a)

exit()
