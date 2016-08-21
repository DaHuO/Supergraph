def base_10_to_2(n):
    return '{0:b}'.format(n)

def base_2_to_b(coin, b):
    return sum([b**i * int(c) for i, c in enumerate(coin[::-1])])

def coin_generator_f(N):
    coin_base10 = 2 ** (N-1) + 1
    max_val = 2 ** N
    while coin_base10 <= max_val:
        yield base_10_to_2(coin_base10)
        coin_base10 += 2
    raise Exception('reached upper limit of coins of length {}'.format(N))

def get_divisor(n):
    giveup = 10000
    for i in xrange(2, giveup):
        if n % i == 0:
            return i
    return None

def test_coin(coin):
    def test_coin_base_n(coin, n):
        coin_base_n = base_2_to_b(coin, n)
        return get_divisor(coin_base_n)
    divisors = []
    for i in range(2, 11):
        divisor = test_coin_base_n(coin, i)
        if not divisor:
            return None
        else:
            divisors.append(divisor)        
    return divisors

def prove_coin(coin, divisors):
    for i in range(2, 11):
        coin_base_n = base_2_to_b(coin, i)
        if coin_base_n % divisors[i - 2] != 0:
            print 'INVALID COIN: ', coin, divisors

def print_divisors(coin, divisors):
    print coin, ' '.join([str(x) for x in divisors])
    
def main():
    T = int(raw_input())
    N, J = map(int, raw_input().split())
    
    print 'Case #{0}:'.format(1)
    coin_generator = coin_generator_f(N)
    coins_produced = 0
    while coins_produced < J:
        coin = next(coin_generator)
        divisors = test_coin(coin)
        if divisors:
            coins_produced += 1
            print_divisors(coin, divisors)
            #prove_coin(coin, divisors)
if __name__ == "__main__":
    main()        
