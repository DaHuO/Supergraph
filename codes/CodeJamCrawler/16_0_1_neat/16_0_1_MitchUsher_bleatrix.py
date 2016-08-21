#!python3

def analyze(num):
    seen = set()
    for x in range(1, 2000):
        seen |= set(*(str(x*num).split()))
        if len(seen) == 10:
            return x*num
    else:
        return 0

def main(tests):
    results = []
    for test in tests:
        results.append(analyze(test))
    
    for i, result in enumerate(results):
        if result == 0:
            print("Case #%s: INSOMNIA" % str(i+1))
        else:
            print("Case #%s: %s" % (str(i+1), str(result)))

if __name__ == '__main__':
    import sys
    T = int(sys.stdin.readline())
    
    tests = []
    while T > 0:
        tests.append(int(sys.stdin.readline()))
        T = T-1
        
    main(tests)