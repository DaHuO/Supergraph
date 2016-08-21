import sys
import utils

def prime_or_div(n):
    for i in range(3, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return -1


def get_val(n, base):
    ncopy = list(n)
    ncopy.reverse()

    val = 0
    for idx, dig in enumerate(ncopy):
        val += int(dig) * (base ** idx)

    return val

def increment(n):
    ncopy = list(n)
    ncopy.reverse()
    
    i=1

    while i < (len(ncopy) - 1):
        if ncopy[i] == '0':
            ncopy[i] = '1'
            ncopy.reverse()
            return ''.join(ncopy)
        else:
            ncopy[i] = '0'
        i += 1

    raise AssertionError('Ran outta numbers')

def get_jamcoins(N, J):
    n = '1' + ('0' * (N-2)) + '1'
    j_list = []

    while len(j_list) < J:
        divisors = [n]

        for i in range(2, 11):
            v = get_val(n, i)
            d = prime_or_div(v)
            if d == -1:
                break
            divisors.append(str(d))


        if len(divisors) == 10:
            j_list.append(divisors)

        if n != ('1' * N):
            n = increment(n)

    return j_list

if __name__ == '__main__':
    fname = sys.argv[1]
    with open(fname) as f, open(fname + '.out', 'w') as fout:
        num_tests = int(f.readline().strip())
        for i in range(num_tests):
            N, J = [int(x) for x in f.readline().strip().split()]
            jcoins = get_jamcoins(N, J)
            fout.write('Case #' + str(i+1) + ':\n')
            for jcoin in jcoins:
                fout.write(' '.join(jcoin) + '\n')
