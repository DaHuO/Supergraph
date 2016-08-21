import sys

def binary(x, n):
    return format(x, 'b').zfill(n)

def anyfactor(n):
    for f in xrange(3, int(n**0.5)+1, 2):
        if n % f == 0:
            return f
    return False

def is_coinjam(s):
    ret = []
    for b in range(2,11):
        f = anyfactor(int(s, b))
        if(not f):
            return False
        ret.append(f)
    return ret

N = 32
J = 500
seen = 0

import signal

class TimeoutException(Exception):   # Custom exception class
    pass

def timeout_handler(signum, frame):   # Custom signal handler
    raise TimeoutException

# Change the behavior of SIGALRM
signal.signal(signal.SIGALRM, timeout_handler)



print 'Case #1:'
for i in xrange(2**(N-2)):
    s = '1' + binary(i, N-2) + '1'
    signal.alarm(1)
    try:
        val = is_coinjam(s)
        if(val):
            seen += 1
            print s, ' '.join(map(str, val))
            sys.stdout.flush()
            if(seen == J):
                sys.exit(0)
    except TimeoutException:
        continue
    else:
        signal.alarm(0)

        
