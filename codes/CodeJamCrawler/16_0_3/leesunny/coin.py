import math

def main():
    i = 0
    while True:
        try:
            t = input()
            if i != 0:  # Skip first line
                print("Case #{}:".format(i))
                coin(t)
        except EOFError:
            break
        i += 1


def parse_coin(s):
    return (int(x) for x in s.rstrip().split(" "))


def coin(c):
    (n, j) = parse_coin(c)
    coin_gen = generate_coin_candidates(n)

    good_coins = []

    while len(good_coins) < j:
        candidate = next(coin_gen)
        divisors = get_divisors(candidate)
        if divisors is not None:
            good_coins.append((candidate, divisors))

    for cn, divs in good_coins:
        print("{} {}".format(cn, " ".join([str(x) for x in divs])))


def generate_coin_candidates(n):
    num = 2**(n-1) + 1
    while num < 2**n:
        yield bin(num)[2:]
        num += 2


def get_divisors(c):
    divisors = []
    for base in range(2, 11):
        num = interpret_in_base(c, base)
        d = first_divisor(num)
        if d is not None:
            divisors.append(d)
        else:
            return None

    return divisors


def first_divisor(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return i

    return None


def interpret_in_base(c, base):
    # print("interpret_in_base: c{}, base{}".format(c, base))
    total = 0
    digits = list(c)
    for i, x in enumerate(reversed(digits)):
        # print("i{}, x{}".format(i, x))
        if int(x) == 1:
            total += base**i
    return total


if __name__ == "__main__":
    main()
