import utils, random

def checkJamCoin(numstr):
    # print 'check#', numstr
    ntd = []
    for j in xrange(2, 11):
        n = int(numstr, j)
        # print 'base:',j, 'num:',n
        if utils.is_prime(n)==False:
            k=utils.smallestdivisor(n)
            # print 'divisor:', k
            if k!=n:
                ntd.append(str(k))
    # print ntd
    if len(ntd)==9:
        print numstr, ' '.join(ntd)
        return True
    return False
def check(numstr, i, N, J):

    if (i==N):
        numstr += "1"
        return [numstr]
    numbers1 = check(numstr+"0", i+1, N, J)
    numbers2 = check(numstr+"1", i+1, N, J)
    return numbers1 + numbers2


    # check(num, i, N)
    # check(num + (10**i), i ,N)

def solve(inval):
    [N,J] = map(lambda x: int(x), inval.split(" "))
    numbers = check("1", 1, N-1, J)
    count = 0
    for numstr in numbers:
        if checkJamCoin(numstr):
            count +=1
            if count==J:
                break
    # print numbers
    # generate N-2



if __name__ == "__main__":
    testcases = input()
    for caseNr in xrange(1, testcases+1):
        inval = raw_input()
        print("Case #%i:" % caseNr)
        solve(inval)
