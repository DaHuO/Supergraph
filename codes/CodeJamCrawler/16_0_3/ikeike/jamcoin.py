import sys
from math import sqrt
from itertools import combinations

stream = sys.stdin

t = int(stream.readline().strip())
n, j = stream.readline().split()
n, j = int(n), int(j)

os = sys.stdout

def divisor(num_bin):
    '''
    return False if prime, list of propor divisors otherwise.
    '''
    l = []
    for k in [2, 4, 6, 8]:
        num = int(num_bin, base=k)
        for i in xrange(3,int(sqrt(num))+1, 2):
            if num%i==0:
                l.append(i)
                break
            if i>600:
                break
    if len(l)==4:
        return [l[0]] + [2] + [l[1]] + [2] + [l[2]] + [2] + [l[3]] + [2] + [3]
    else:
        return False

def generate(n):
    k = 1
    while 3*k+1<n-2:
        pos = combinations(range(0,n-2), 3*k+1)
        for p in pos:
            # reset s to 0
            s = ['0']*(n-2)
            for i in p:
                # set 1's
                s[i] = '1'
            s = ['1'] + s + ['1']
            yield ''.join(s)
        k += 2

def find(n, j):
    # keys are jamcoins, values are list of divisors
    div = {}
    while len(div)<j:
        # generate a jamcoin
        for num_bin in generate(n):
            d = divisor(num_bin)
            if d:
                div[num_bin] = d
                if len(div)>=j:
                    break
    return div

# in the middle even number of 1's
# 3*k+1 number of 1's where k is odd
# 4, 10, 16, 22, 28
#
#

#
# in the middle of the number (in 14/30 bits)
# yield permutations of 3k+11's, where k is even. 1, 7, 13 / 1, 7, 13, 19, 25
# check primality of generated numbers for base 2,4,6,8
#

div = find(n, j)
os.write('Case #1:\n')
# print binary jamcoin then proof of divisors
for coin in div:
    os.write(coin + ' '),
    for d in div[coin]:
        os.write(str(d)+' ')
    os.write('\n')
