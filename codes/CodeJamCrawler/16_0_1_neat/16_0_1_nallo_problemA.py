
def solve(test_case):
    N = int(raw_input())

    if N==0:
        print "Case #" + str(test_case) + ": INSOMNIA"
        return

    n = N
    digits_to_see = set([i for i in xrange(10)])
    while 1:
        for d in str(n):
            digits_to_see.discard(int(d))
            if len(digits_to_see)==0: break


        if len(digits_to_see)==0: break
        else: n += N

    print "Case #" + str(test_case) + ": " + str(n)
    return

def main():
    t = int(raw_input())
    for i in  xrange(t):
        solve(i+1)

if __name__=="__main__":
    main()
