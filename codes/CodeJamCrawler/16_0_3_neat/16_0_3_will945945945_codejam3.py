def prime(n):
    if n == 1 or n == 0:
        return 'No'
    elif n % 2 == 0 and n != 2:
        return '2'
    else:
        theta = n**0.5
        k = 3
        while n % k != 0:
            k += 2
            if k >= theta:
                return 'Prime'
                break
        return str(k)

def f(N,J):
    N = int(N)
    J = int(J)
    
    Ans = []
    for i in xrange(0,2**(N-2)):
        b = bin(i)[2:]
        cand = '1' + '0'*(N-2-len(b)) + b + '1'
        C = [int(cand,j) for j in xrange(2,11)]
        C = map(prime, C)
        if 'Prime' in C or 'No' in C:
            continue
        else:
            Ans += [cand + ' ' + reduce(lambda x,y:x+' '+y,C) ]

        print len(Ans),J
        if len(Ans) == J:
            return Ans
    return Ans

F = open('C-small-attempt0.in')
A = F.read()
A = A.split('\n')[1:-1]
A = A[0].split(' ')
Ans = f(A[0],A[1])

E = open('Ans3.small','w')
E.write('Case #1:\n')
for i in xrange(len(Ans)):
    E.write( Ans[i] + '\n')
E.close()   


