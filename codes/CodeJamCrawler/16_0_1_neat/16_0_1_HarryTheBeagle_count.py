
def count(N):
    if N == 0:
        return "INSOMNIA"

    seen = set()
    for i in range(10):
        seen.add(i)

    i = 1
    last_num = num = None
    while seen:
        last_num = num = N * i
        while num != 0 and seen:
            digit = num % 10
            num /= 10
            if digit in seen:
                seen.remove(digit)
        i += 1
    return last_num  
    

if __name__ == "__main__":
    T = int(raw_input())
    for i in xrange(T):
        N = int(raw_input())
        print "Case #{}: {}".format(i + 1, count(N))


