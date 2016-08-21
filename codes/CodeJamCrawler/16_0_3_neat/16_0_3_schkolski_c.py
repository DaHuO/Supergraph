def solve(n, j):
    primes = set([])

    def is_prime(num):
        if num <= 0: return False
        if num == 1 or num == 2: return True
        if num in primes:
            return True
        for i in range(2, int(num ** .5) + 1):
            if num % i == 0:
                return False
        primes.add(num)
        return True

    def get_binary(k, length):
        res = '{0:b}'.format(k)
        while len(res) < length:
            res = '0' + res
        return res

    def is_jamcoin(bnum):
        for i in xrange(2, 11):
            tmp = int(bnum, i)
            if is_prime(tmp):
                return False
        return True

    def find_div(num):
        for i in xrange(2, num):
            if num % i == 0:
                return i
        return num

    def get_proof(bnum):
        divs = []
        for k in xrange(2, 11):
            tmp = int(bnum, k)
            div = find_div(tmp)
            divs.append(div)
        return divs

    
    jamcoins = []
    _all = [get_binary(i, n - 2) for i in xrange(2 ** (n - 2))]

    for curr in _all:
        curr = '1{0}1'.format(curr)

        if is_jamcoin(curr):
            j -= 1
            proof = get_proof(curr)
            jamcoins.append('{0} {1}'.format(curr, ' '.join([str(elem) for elem in proof])))
        
        if j == 0: break
    
    return '\n'+'\n'.join(jamcoins)


import time
if __name__ == "__main__":
    FILENAME = 'C-small-attempt1.in'
    lines = open(FILENAME, 'r').read().split('\n')
    T = int(lines[0])

    for case in xrange(1, T+1):
        data = lines[case].split(' ')

        answer = solve(int(data[0]), int(data[1]))
        print "Case #{0}: {1}".format(case, answer)
