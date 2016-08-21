import sys

def find_sleep(n):
    def set10(s):
        if len(s) != 10:
            return False
        for n in s:
            if n < 0 and n > 9:
                return False
        return True
    
    nums = set()
    
    if n == 0:
        return 'INSOMNIA'
    multiplier = 0;
    val = 0
    while not set10(nums):
        multiplier += 1
        val = n * multiplier
        for c in str(val):
            nums.add(int(c))
    return val

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for _t in xrange(t):
        s = int(f.readline())
        n = str(find_sleep(s))
        print "Case #%d: %s" % (_t+1, n)
