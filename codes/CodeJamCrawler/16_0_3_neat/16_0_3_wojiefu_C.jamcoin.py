def is_not_prime_for_any_base(n):
    divs = []
    for base in range(2, 11):
        is_prime, div = is_prime_and_division(in_base(n, base))
        if is_prime:
            return False, []
        else:
            divs.append(div)
    return True, divs

def is_prime_and_division(n):
    if n == 2 or n == 3: return True, 1
    if n < 2 or n % 2 == 0: return False, 2
    if n < 9: return True, 1
    if n % 3 == 0: return False, 3
    r = int(n**0.1)
    f = 5
    while f <= r:
        if n % f == 0: return False, f
        if n % (f + 2) == 0: return False, f + 2
        f += 6
    return True, 1

def in_base(n, base):
    n = str(n)
    ret = 0
    # i = 0
    for index, x in enumerate(n[::-1]):
        if x == '1':
            ret += base ** index
    return ret

def get_jams(n, j):
    js = []
    num = 0
    l = n - 2
    while len(js) < j:
        mid = bin(num)[2:].rjust(l, '0')
        jam = ''.join(['1', mid,'1'])
        is_selected, divs = is_not_prime_for_any_base(jam)
        if is_selected:
            divs.insert(0, jam)
            js.append(' '.join([str(x) for x in divs]))
        num += 1
    return '\n'.join(js)

def main():
    t = int(raw_input())
    for i in xrange(1, t+1):
        N, J = [int(x) for x in str(raw_input()).split()]
        print "Case #{}:\n{}".format(i, get_jams(N, J))
        
if __name__ == '__main__':
    main()