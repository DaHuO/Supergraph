N = int(input())
for I in range(1, N+1):
    n = int(input())
    if n == 0:
        result = 'INSOMNIA'
    else:
        digits_seen = set()
        i = 1
        while len(digits_seen) is not 10:
            digits_seen = digits_seen.union(set(str(i*n)))
            i += 1
        result = (i-1)*n    
    print("Case #%d: %s" % (I, str(result)))
