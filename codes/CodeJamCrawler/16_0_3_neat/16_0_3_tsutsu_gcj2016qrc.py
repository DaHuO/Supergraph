def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q & 1 == 0: return False
    return pow(2, q - 1, q) == 1

def ham(n):
    for i in range(2, n):
        if n % i == 0:
            return i
    return n

def spam(b):
    if b[-1] == '0': return []
    result = []
    for i in range(2, 11):
        num = int(b, i)
        if is_prime(num):
            return []
        result.append(ham(num))
    return result

with open('C-small-attempt1.in') as f:
    T = int(f.readline()[:-1])
    for i in range(T):
        print('Case #{0}:'.format(i + 1))
        N, J = [int(x) for x in f.readline()[:-1].split()]
        count = 0
        num = int(''.join(['1' if(i == 0) else '0' for i in range(N)]), 2)
        while True:
            if J <= count:
                break;
            b = bin(num).lstrip('0b')
            l = spam(b)
            if len(l) == 9:
                print('{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}'.format(b, l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8]))
                count += 1
            num += 1
