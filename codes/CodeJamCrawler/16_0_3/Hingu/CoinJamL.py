import math
    
def generateBinString(N, J):
    count = 1
    lb = long(math.pow(2, N-1)+1) ## smallest odd number with N bits in its binary rep.
    ub = long(math.pow(2, N)-1) ## largest odd number with N bits in its binart rep.
    while lb <= ub:
        binary = '{0:b}'.format(lb)
        divs = [];
        if count <= J:
            for base in xrange(2, 11):
                d = getnonTrivialDivisor(long(binary, base))
                if d == None:
                    break
                else:
                    divs.append(d)
            else:
                count += 1
                print binary, ' '.join(str(e) for e in divs)
        else:
            break
        lb += 2

def getnonTrivialDivisor(x):
    y = 2; ul = int(math.sqrt(x))
    while y <= ul:
        if x % y == 0:
            return y
            break
        if y > 4000:
            break
        y += 1
    else:
        return None
    
def main():
    for t in xrange(int(raw_input().strip())):
        N, J = raw_input().strip().split()
        N, J = [int(N), int(J)]
        print 'Case #'+str(t+1)+':'
        generateBinString(N, J)
            
if __name__ == '__main__': 
    main()
