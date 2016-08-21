def get_digits(n):
    return map(int, list(str(n)))

def get_last_number(n):
    if not n:
        return 'INSOMNIA'
    digits_seen = [0 for i in range(10)]
    required = [1 for i in range(10)]
    k = 2
    r = n
    while True:
        digits = get_digits(r)
        for d in digits:
            digits_seen[d] = 1
        if digits_seen == required:
            break
        # if k == 1000:
        #     print "Exiting : Could not find all digits"
        #     break
        r = n * k
        k += 1
    # print "Value of k is {} and n is {}".format(k, r)
    return r if digits_seen == required else 'INSOMNIA'

if __name__ == '__main__':
    t = input()
    for i in xrange(t):
        n = input()
        print "Case #{}: {}".format(i+1, get_last_number(n))