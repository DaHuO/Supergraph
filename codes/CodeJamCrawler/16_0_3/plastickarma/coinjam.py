def bit_generator(size):
    middle_size = size - 2
    counter = 0
    while True:
        next_number = '1' + "{0:b}".format(counter).rjust(middle_size, '0') + '1'
        counter += 1
        yield next_number


def get_divisor(decimal_number):
    if decimal_number % 2 is 0:
        return 2

    for divisor in range(3, 10000, 2):
        if decimal_number % divisor is 0:
            return divisor


def generate_jamcoins(length):
    bg = bit_generator(length)

    while True:
        jc = generate_jamcoin(next(bg))
        if jc is not None:
            yield jc

def generate_jamcoin(bit_string):
    divisors = []
    is_prime = False
    for base in range(2, 11):
        decimal_number = int(bit_string, base)

        divisor = get_divisor(decimal_number)
        if divisor is not None:
            divisors.append(divisor)
        else:
            break

    if len(divisors) is 9:
        return bit_string, divisors


no_of_testcases = input()
length, no_of_coins = input().split()
length = int(length)
no_of_coins = int(no_of_coins)

jamcoin_generator = generate_jamcoins(length)
print("Case #1:")
for i in range(0, no_of_coins):
    coin, divisors = next(jamcoin_generator)
    print(coin, ' '.join([str(d) for d in divisors]))


