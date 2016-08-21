import sys

inf = sys.argv[1]

f = open(inf, 'rU')
outf = open(inf + ".out", 'w')

T = int(f.readline())
for t in xrange(T):
    outf.write("Case #{0}:\n".format(t+1))
    (N, J) = (int(x) for x in f.readline().split())

    j = 1

    primes = [2, 3]
    for x in xrange(5, 100):#10**((N+1)/2)):
        prime = True
        for p in primes:
            if p*p > x:
                break
            if x % p == 0:
                prime = False
                break
        if prime:
            primes.append(x)

    for i in xrange(2**(N-2)):
        to_format = '1{0:0%db}1' % (N-2)
        num = to_format.format(i)
        all_noprime = True
        divisible_by = []
        for base in xrange(2, 11):
            num_in_base = int(num, base)
            divisible = False
            for p in primes:
                if p*p > num_in_base:
                    break
                if num_in_base % p == 0:
                    divisible_by.append(p)
                    divisible = True
                    break
            if not divisible:
                all_noprime = False
                break
        if all_noprime:
            print "FOUND ONE", num
            outf.write("{0} {1}\n".format(num, " ".join([str(x) for x in divisible_by])))
            j += 1
            if j > J:
                break

    #outf.write("Case #{0}".format(n+1))

f.close()
outf.close()
