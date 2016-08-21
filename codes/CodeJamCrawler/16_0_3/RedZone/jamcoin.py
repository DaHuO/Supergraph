from math import sqrt

input()
N, J = map(int, raw_input().split())

def factor(num):
    if num % 2 == 0:
        return 2
    for i in xrange(3, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            return i
    return num

i = int('1%s1' % ('0' * (N - 2)), 2)
print 'Case #1:'

total_coins = 0

while total_coins < J:
    coin = '{0:b}'.format(i)
    proofs = []
    for b in xrange(2, 11):
        num = int(coin, b)
        smallest_factor = factor(num)
        if smallest_factor == num:
            break
        proofs.append(str(smallest_factor))

    if len(proofs) == 9:
        total_coins += 1
        print coin, ' '.join(proofs)
    i += 2
