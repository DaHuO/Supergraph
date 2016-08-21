def flip(lb, ub, p):
    s = ''
    for i in p[lb:ub]:
        if i == '-':
            s+='+'
        else:
            s+='-'
    return s[::-1]+p[ub:]

def executeManeuver(p):
    optimalFlip = 0
    while p.count('-') != 0:
        if (p.count('-') == len(p)):
            optimalFlip += 1
            p = flip(0, len(p), p)
            break
        if(p[0] == '+'):
            firstIofM = p.index('-')
            #print firstIofM
            optimalFlip += 1
            p = flip(0, firstIofM, p)
            #print p
        if (p.count('-') == 0):
            break
        if (p.count('-') == len(p)):
            optimalFlip += 1
            p = flip(0, len(p), p)
            break
        firstIofP = p.index('+')
        #print firstIofP
        optimalFlip += 1
        p = flip(0, firstIofP, p)
        #print p

    return optimalFlip

def main():
    for t in xrange(int(raw_input().strip())):
        panCakeStack = raw_input().strip()
        print 'Case #'+str(t+1)+':', executeManeuver(panCakeStack)
            
if __name__ == '__main__': 
    main()
