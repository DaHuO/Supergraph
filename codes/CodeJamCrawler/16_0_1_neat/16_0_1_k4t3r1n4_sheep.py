import sys

def get_digits(N):
    return [int(digit) for digit in str(N)]

def get_last_number_beatrix_names(N):
    digits = set()
    iN = N
    digits.update(get_digits(iN))
    while len(digits) < 10:
        iN += N
        digits.update(get_digits(iN))
    return iN

T = int(sys.stdin.readline())
for t in xrange(T):
    N = int(sys.stdin.readline())
    if N:
        print 'Case #' + str(t+1) + ': ' + str(get_last_number_beatrix_names(N))
    else:
        print 'Case #' + str(t+1) + ': INSOMNIA'
