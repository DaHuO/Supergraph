input_file_name = "C-small-attempt0"
output_file=open("{}.out" .format(input_file_name),'a')
import itertools
from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def factors(n):
    for x in xrange(2,n+1):
        if (n % x) == 0:
            return x


def getCoinJam(N):
    n, j= N.split()
    prime = set([])
    n = int(n)
    j= int(j)
    count = 0
    result = []
    lst = list(itertools.product([0, 1], repeat=n-2))
    for var in lst:
        if count >= j:
            break
        var = (1,) + var + (1,)
        coinjams = []
        varStr = ''.join(str(i) for i in var)
        compute = []
        is_prime = False
        for i in xrange(2, 11):
            val = int(varStr, i)
            compute.append(val)
            if val in prime:
                break

            if isPrime(val):
                prime.add(val)
                is_prime = True
                break

        if not is_prime:
            count = count + 1
            coinjams.append(varStr)
            for computeVal in compute:
                coinjams.append(factors(computeVal))
            result.append(" ".join(str(item) for item in coinjams))
    return result

with open("{}.in".format(input_file_name)) as input_file:
    counter= 0
    try:
        totalInput=long(input_file.readline())
        for i in range(totalInput):
            value=getCoinJam(input_file.readline())
            output_file.write("Case #{}: ".format(i+1)+"\n")
            for i , j in enumerate(value):
                if i == len(value) - 1:
                    output_file.write("{}".format(str(j)))
                else:
                    output_file.write("{}".format(str(j))+"\n")

    except Exception as e:
        pass


print "done"
output_file.close()
