from sympy.ntheory import factorint


def output(t, res):
    casestr = "Case #" + str(t+1) +":"
    status = str(res) if res != None else "impossible"
    outputLine = casestr+status
    print outputLine



def testJamCoin(jc):
    res = [] 
    for base in xrange(2, 11):
        val = int(jc, base)
        divisors = factorint(val)
        for d in divisors:
            if d == val:
                return None
            else:
                res.append(d)
                break

    return res

def main():


    ############################################1
    T = int( raw_input() )
    for t in xrange(T):    
        N, J = map( int, raw_input().split(' ') )
        output( t, "" )
        found = 0
        binLastNum = '1' + '0'*(N-2) + '1'
        lastNum = int(binLastNum, 2)
        while found < J:
            res = testJamCoin(binLastNum) 
            if not res == None:
                print binLastNum, " ".join(map(str, res))
                found += 1
            lastNum += 2
            binLastNum = bin(lastNum)[2:]




if __name__ == "__main__":
   main()