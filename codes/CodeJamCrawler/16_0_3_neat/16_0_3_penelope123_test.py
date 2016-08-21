f = open('C-large.in')
length = int(f.readline())
cases = [f.readline().strip() for i in range(length)]

# setup some basic primes
known_primes = [2,3]
#for i in range(3,100000,2):
for i in range(3,10000,2):
    divides_by = None
    for j in known_primes:
        if i % j == 0:
            divides_by = j
    if not divides_by:
        # it's prime!
        known_primes.append(i)
#print known_primes

# The magic is that we don't worry about assuming a number is prime when it's actually not.
def divider(number):
    for j in known_primes:
        if number % j == 0:
            return j
    return None

for i, case in enumerate(cases):
    n,j = [int(k) for k in case.split()]
    print "Case #%s:" % (i+1)
    # print n,j

    # generate some jamcoins
    for k in xrange(2**(n-2)):
        # generate the binary string
        bits = []
        for l in range(1,n-1):
            mod = k % (2**l)
            if mod:
                bits.insert(0,"1")
                k -= mod
            else:
                bits.insert(0,"0")
        string = "1%s1" % ''.join(bits)

        # print "testing", string
        result = string
        passes = True
        for base in range(2,11):
            # print base
            equiv = int(string, base)
            # print equiv
            # is this prime?
            d = divider(equiv)
            if d:
                result += " " + str(d)
            else:
                passes = False
                # print "fails"
                break

        if passes:
            print result
            j -= 1
            if j <= 0:
                # print "I've found enough"
                break

