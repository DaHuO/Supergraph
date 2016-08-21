def memorize(number, arr):
    for i in range(0,10):
        s = str(i)
        if s in number:
            arr = arr[:i] + "_" + arr[i + 1:]
    return arr

def check(arr):
    return '*' not in arr

#for N in range (1, 1000000):
#for N in range (1692, 1693):
def solve(N):
    if N == 0:
        return "INSOMNIA";
    arr = "**********"
    order = 10 ** len(str(N))
    prevFirstDigit = 0
    for i in range(1, 102):
        if prevFirstDigit == 9:
            break;
        else:
            res = i * N;
    #            print "old arr: %s" % arr
            arr = memorize(str(res), arr)
    #            print "new arr: %s" % arr
            if check(arr):
                return str(res)
            firstDigit = res / order;
            if firstDigit != prevFirstDigit and firstDigit != prevFirstDigit + 1:
                print "Found an N: %d, which may not produce all digits" % N
                quit;
            prevFirstDigit = firstDigit;

def main():
    testcases = int(raw_input()) 
    for case in xrange(1, testcases + 1):
        N = int(raw_input())
        print "Case #%d: %s" % (case, solve(N))

if __name__ == "__main__":
    main()
