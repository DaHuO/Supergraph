from itertools import product


BASES = range(2, 11)


def generate_coins(length):
    def is_valid(coin):
        return coin[0] == "1" and coin[-1] == "1"

    digits_product = list(product("01", repeat=length))
    digits_valid = list(filter(is_valid, digits_product))
    coins = list(map(lambda x: "".join(x), digits_valid))

    return sorted(coins)


def generate_representations(coin):
    return [int(coin, base=curr_base) for curr_base in BASES]


def is_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if not number % divisor:
            return (False, divisor)

    return (True, None)


def valid_jamcoin(coin):
    representations = generate_representations(coin)
    divisors = []

    for representation in representations:
        prime, divisor = is_prime(representation)
        divisors.append(divisor)

        if prime:
            return (False, None)

    return (True, divisors)


def find_jamcoins(length, amount):
    coins = generate_coins(length)
    jamcoins = []

    for coin in coins:
        if len(jamcoins) >= amount:
            break

        jamcoin, divisors = valid_jamcoin(coin)

        if jamcoin:
            jamcoins.append((coin, divisors))

    return jamcoins


def format_jamcoin(jamcoin, divisors):
    return "{} {}".format(jamcoin, " ".join(map(str, divisors)))


def print_jamcoins():
    length, amount = map(int, input().split())

    for jamcoin, divisor in find_jamcoins(length, amount):
        print(format_jamcoin(jamcoin, divisor))

if __name__ == '__main__':
    tests = int(input())

    for idx in range(1, tests + 1):
        print("Case #{}:".format(idx))
        print_jamcoins()
