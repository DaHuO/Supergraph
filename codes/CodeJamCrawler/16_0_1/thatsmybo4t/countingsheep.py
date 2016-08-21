def complete(digits):
    for d in digits:
        if not d:
            return False
    return True

def update(digits, n):
    for l in str(n):
        digits[int(l)] = True

def solve():
    n = input()
    digits = [False] * 10
    if n == 0:
        return "INSOMNIA"
    m = 1
    update(digits, n)
    while not complete(digits):
        m += 1
        update(digits, m*n)
    return str(m*n)
    

def main():
    t = input()
    for i in xrange(1,t+1):
        ans = str(solve())
        print "Case #%d: %s" % (i,ans)

if __name__ == "__main__":
    main()
