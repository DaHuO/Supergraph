import itertools


def is_not_prime(n):
    if n == 2 or n == 3: return ''
    if n < 2 or n%2 == 0: return '2'  # instead of True
    if n < 9: return ''
    if n%3 == 0: return '3'   # instead of True
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return str(f)   # instead of True
        if n%(f+2) == 0: return str(f+2) #instead of True
        f +=6
    return ''


def creat_jamcoin(n, j):
    result = []
    count = 0
    for i in itertools.product(['0', '1'], repeat=n-2):
        gen = '1' + ''.join(i) + '1'
        y = [str(is_not_prime(int(gen, b))) for b in range(2,11)]
        if all(y):
            result.append(gen + ' ' + ' '.join(y))
            count += 1
            if count == j:
                return result


t = int(input())    # which is always 1!

for i in range(1, t+1):
    N, J = map(int, input().split(' '))
    print("Case #{}:".format(i))
    for r in creat_jamcoin(N, J):
        print(r)
