def isPrime(n):
    if n==2 or n==3: return True, 0
    if n%2==0 or n<2: return False, 2
    for i in xrange(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False, i    

    return True, 0


T = int(raw_input())


for t in range(T):
    N, J = map(int, raw_input().split())

    print "Case #%d:" %(t+1)
    top = int('1' + ('1'*(N-2)) +  '1', 2)
    botton = int('1' + ('0'*(N-2)) +  '1', 2)
    jamcoins = []


    for i in xrange(botton, top + 1):
        n = "{0:b}".format(i)

        if n[0] != '1' or n[-1] != '1':
            continue

        n2, d2 = isPrime(int(n, 2))
        n3, d3 = isPrime(int(n, 3))
        n4, d4 = isPrime(int(n, 4))
        n5, d5 = isPrime(int(n, 5))
        n6, d6 = isPrime(int(n, 6))
        n7, d7 = isPrime(int(n, 7))
        n8, d8 = isPrime(int(n, 8))
        n9, d9 = isPrime(int(n, 9))
        n10, d10 = isPrime(int(n, 10))

        if (not n2) and (not n3) and (not n4) and (not n5) and (not n6) and (not n7) and (not n8) and (not n9) and (not n10):
            jamcoins.append((n, d2, d3, d4, d5, d6, d7, d8, d9, d10))
            J -= 1

        if J == 0:
            break

    for jc in jamcoins:
        print jc[0], ' '.join(map(str, jc[1:]))

