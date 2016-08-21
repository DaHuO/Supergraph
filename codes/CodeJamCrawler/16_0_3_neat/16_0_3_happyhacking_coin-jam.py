import math
def find_divisor(n):
    stop = int(math.sqrt(n) + 1)
    for i in range(2, stop):
        if n % i == 0:
            return i
    return 0

def main():
    T = int(raw_input())
    raw = raw_input().split()
    N, J = int(raw[0]), int(raw[1])
    base10 = 2 ** (N-1) + 1
    print 'Case #1:'
    while J:
        binary_str = bin(base10)[2:]
        #print binary_str
        res = []
        for base in range(2, 11):
            n = int(binary_str, base)
            #print 'base %s: %s' % (base, n)
            div = find_divisor(n)
            if div == 0:
                break
            res.append(str(div))
        if len(res) == 9:
            res.insert(0, binary_str)
            print '%s' % ' '.join(res)
            J -= 1
        base10 += 2

if __name__ == '__main__':
    main()
