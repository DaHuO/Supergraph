import sys, fileinput, math


def generate_candidates(N):
    """generates candidate strings of length N in binary"""
    format_string = '1{0:0%db}1' % (N-2)
    for i in xrange(int(2**(N-2))):
        candidate = format_string.format(i)
        yield candidate


# performance hack: we drop a lot of potential jamcoins which might be divisible
# by primes > 37, but we know we have so many of them it doesn't matter.
# proper way to do this would be to get a list of all primes, but that's
# not so trivial given the max prime we look for is at around sqrt(10^32)
known_primes = [2,3,7,11,13,17,19,23,29,31,37]

            
def get_divisor(n):
    """returns a non-trivial divisor of n, if it exists"""
    for i in known_primes: 
        if n%i == 0:
            return i

        
def is_jamcoin(c):
    """returns an array with the jamcoin c in binary and divisors in base 2-9 if c is not prime in any, otherwise None"""
    output = [c,]
    for base in range(2,11):
        in_base = int(c, base)
        p = get_divisor(in_base)
        if not p:
            return
        output.append(str(p))
    return output



def test_generator():
    """make sure candidates are properly generated"""
    case_3 = list(generate_candidates(3))
    assert(case_3 == ['101','111'])

    case_4 = list(generate_candidates(4))
    assert(case_4 == ['1001', '1011', '1101', '1111'])

def test_example():
    """make sure examples from description work"""
    assert(is_jamcoin('100011'))
    assert(is_jamcoin('111111'))
    assert(is_jamcoin('111001'))

    
if __name__ == '__main__':
    for (linenr, line) in enumerate(fileinput.input()):
        line = line.replace('\n', '')
        
        if fileinput.isfirstline():
            n = int(line)
            continue
        
        if linenr>n:
            print 'too many input lines (?)'
            break

        print "Case #%d:" % linenr        

        [N,J] = [int(i) for i in line.split(' ')]

        found = 0
        for candidate in generate_candidates(N):
            confirmation = is_jamcoin(candidate)
            if not confirmation:
                continue
            print " ".join(confirmation)

            """
            for base in range(2, 11):
                d = int(confirmation[base-1])
                num = int(confirmation[0], base)
                print '  %2d: %d = %d * %s' % (base, num, d, num/d)
            """

            
            found += 1
            if found == J:
                sys.exit()
            

