import math


def is_prime(n):
    if n == 2:

        return 0
    if n % 2 == 0 or n <= 1:
        return 2

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        # Only for threshold purpose, if divisor is too big, assume it's prime and discard
        if divisor > 11:
            return 0

        if n % divisor == 0:
            return divisor

    return 0


def base_i(base, base_binary):
    binary_str = "{0:b}".format(base_binary)
    value = 0
    length = len(binary_str)
    for ind in range(length):
        digit = int(binary_str[ind])
        if digit == 1:
            d = length - ind - 1
            value += digit * (base ** d)

    return value


def odd_ones(x):

    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1

    return x & 1


def verify_legit(num, base_num):

    is_legit = True

    # Get base value
    base_value = base_i(base_num, num)

    # calculate prime
    divisor_value = is_prime(base_value)

    if divisor_value == 0:
        is_legit = False
        return {'divisor_value': divisor_value, 'is_legit': is_legit}

    return {'divisor_value': divisor_value, 'is_legit': is_legit, 'base_value': base_value}


def main():
    of = open('coin-large.out', 'w', 1)

    with open('C-large.in', 'r') as f:
        count = int(f.readline().rstrip('\n'))
        for i in range(count):
            line = f.readline().rstrip('\n')
            nums = line.split(' ')
            number = int(nums[0])
            sample_count = int(nums[1])
            of.write('Case #{}:\n'.format(i+1))

            for num in range(2 ** (number - 1) + 1, 2 ** number, 2):

                is_legit = True

                bases = []

                for base_num in range(2, 11):

                    result = verify_legit(num, base_num)
                    is_legit = result['is_legit']
                    if not is_legit:
                        break
                    divisor_value = result['divisor_value']
                    bases.append(divisor_value)

                if is_legit:
                    bin_str = "{0:b}".format(num)
                    of.write(bin_str)

                    for v in bases:
                        of.write(' {}'.format(v))

                    sample_count -= 1
                    if sample_count <= 0:
                        break
                    of.write('\n')

    of.close()

if __name__ == "__main__":
    main()
