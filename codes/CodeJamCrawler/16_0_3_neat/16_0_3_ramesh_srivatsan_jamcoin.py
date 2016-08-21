
N = 32
J = 500
limit = (1e16-1)//9
limit = int(limit)
# a = [True] * limit                          # Initialize the primality list
#
# def primes_sieve2():
#     global a
#     a[0] = a[1] = False
#
#     for (i, isprime) in enumerate(a):
#         if isprime:
#             yield i
#             for n in xrange(i*i, limit, i):     # Mark factors non-prime
#                 a[n] = False

def factor(n):
    for i in xrange(2, 9999999):
        if n%i==0:
            return i
    return 0

k = i = 0
print 'Case #1:'
while k<J:
    ss = '1'+('{0:0'+str(N-2)+'b}').format(i)+'1'
    lis = [str(factor(int(ss,b))) for b in range(2,11)]
    try:
        lis.index('0')
        i+=1
        continue
    except:
        print(ss+' '+(' '.join(lis)))
        k+=1
        i+=1


