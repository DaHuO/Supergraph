def is_prime(n): # assume n > 10
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n%p == 0: return p

    r = min( int(n**0.5), 1000)
    f = 5
    while f <= r:
        if n%f == 0: return f
        if n%(f+2) == 0: return f+2
        f += 6
    return n

N = 32;
J = 500;
num0 = int("1" + "0" * (N-2) + "1", base = 2);
jamcoin = [int("{0:b}".format(num0), base = b) for b in range(2, 11)];
cnt = 0;

print "Case #1:"
while cnt<J:
    s = str("{0:b}".format(num0))
    jc = True
    for i in jamcoin:
        f = is_prime(i)
        if f != i:
            s += " " + str(f)
        else:
            jc = False
            break
    if jc:
        cnt += 1
        print s

    num0 += 2
    jamcoin = [int("{0:b}".format(num0), base = b) for b in range(2, 11)];








