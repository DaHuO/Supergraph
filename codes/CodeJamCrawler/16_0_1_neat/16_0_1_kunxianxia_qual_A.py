t = int(raw_input())

for i in xrange(1, t+1):
    N = raw_input()
    n = int(N)
    if n > 0:
        bitmap = [False for j in xrange(10)]
        P = [0 for j in xrange(len(N))]
        N = [int(N[-j]) for j in xrange(1, len(N)+1)]
        while (True):
            carry = 0
            for j in xrange(len(N)):
                carry,P[j] = divmod(P[j]+N[j] + carry, 10)
                bitmap[P[j]] = True
            for j in xrange(len(N),len(P)):
                carry,P[j] = divmod(P[j]+carry, 10)
                bitmap[P[j]] = True
            if carry > 0:
                bitmap[carry] = True
                P.append(carry)
            AND = True
            for j in xrange(10):
                if bitmap[j]:
                    AND = True
                else:
                    AND = False
                    break
            if AND:
                print "Case #{}: {}".format(i, "".join([str(P[-j]) for j in xrange(1,len(P)+1)]))
                break
    else:
        print "Case #{}: INSOMNIA".format(i)
