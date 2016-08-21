import math
import random

input_file = "C-large.in"
output_file = "C-large.out"

def main():
    results = []
    
    f = open(input_file, 'r')
    T = int(f.readline())
    for t in range(T):
        N,J = f.readline().split()
        jamcoins = generate_jamcoins(int(N),int(J))
        results.append(jamcoins)
    f.close()

    f_out = open(output_file, 'w')
    for t in range(T):
        f_out.write('Case #%d:\n' % (t+1))
        for jamcoin in results[t]:
            f_out.write(jamcoin + '\n')
    f_out.close()

def generate_jamcoins(N,J):
    jamcoins = []
    prev_coins = set()
    while (len(jamcoins) < J):
        num_prev = len(prev_coins)
        coin = ''
        while len(prev_coins) == num_prev:
            coin = '1' + ('{0:0%db}'%(N-2)).format(random.getrandbits(N-2)) + '1'
            prev_coins.add(coin)
        is_jamcoin = True
        factors = ''
        for base in range(2, 11):
            value = 0
            for bit in range(N):
                value += int(coin[bit]) * base**(N-bit-1)
            factor = 2
            if value % 2 == 1:
                factor = 3
            composite = False
            threshold = min(math.sqrt(value), 1000000)
            while factor <= threshold and not composite:
                composite = value % factor == 0
                factor += 2
            if composite:
                factors = factors + ' ' + str(factor-2)
            else:
                is_jamcoin = False
                break
        if is_jamcoin:
            jamcoins.append(coin + factors)
    return jamcoins

if __name__ == "__main__":
    main()
