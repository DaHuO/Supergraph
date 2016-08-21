
def main():
    file = open('test', 'rU')
    lines = iter(file.readlines())
    file.close()

    next(lines)
    coin_length, coin_total = [int(x) for x in next(lines).split()]
    number = 2 ** (coin_length - 1) + 1

    output = open('output', 'w')
    print('Case #1:', file=output)
    coin_count = 0

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    while coin_count < coin_total:
        divisors = []
        number_bin = bin(number)[2:]

        for base in range(2, 10):
            base_number = 0
            for bit in range(coin_length):
                if number_bin[bit] is '1':
                    base_number += base ** (coin_length - 1 - bit)

            divisors.append(get_non_trivial_divisor(base_number, primes))
            if divisors[-1] is None:
                break

        if divisors[-1] is not None:
            divisors.append(get_non_trivial_divisor(int(number_bin), primes))

            if divisors[-1] is not None:
                print('{} {}'.format(number_bin, ' '.join(divisors)), file=output)
                coin_count += 1

        number += 2
    output.close()


def get_non_trivial_divisor(number, primes):
    for prime in primes:
        if number % prime == 0:
            return str(prime)
    return None

if __name__ == '__main__':
    main()
