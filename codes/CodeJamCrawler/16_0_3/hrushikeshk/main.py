def convert(num, base):
    max_power = len(str(num)) - 1
    converted_num = 0
    for i in str(num):
        converted_num += int(i) * (base ** max_power)
        max_power -= 1
    return converted_num


def isprime(n):
    """check if integer n is a prime"""
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(int(n ** 0.5) ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def main():
    a = '10000000000000000000000000000001'

    # test = int(raw_input())
    #
    # n,j = raw_input().split()
    count = 0
    print "Case #1: "

    while count != 500:
        base_numbers = list()
        for i in range(9):
            base_numbers.append(convert(a, i+2))

        is_jam_coin = False

        for nums in base_numbers:
            if isprime(nums):
                is_jam_coin = False
                break
            else:
                is_jam_coin = True

        if is_jam_coin:
            divisors = list()
            for i in base_numbers:
                for j in range(2, int(int(i ** 0.5) ** 0.5) + 1):
                    if i % j == 0:
                        divisors.append(j)
                        break

            print a + " " + str(divisors[0]) + " " + str(divisors[1]) + " " + str(divisors[2]) + " " + str(divisors[3]) + " " + str(divisors[4]) + " " + str(divisors[5]) + " " + str(divisors[6]) + " " + str(divisors[7]) + " " + str(divisors[8])
            count += 1

        a = bin(int(a, 2) + int('10', 2))
        a = a.replace('b', '0')
        a = a.strip("0")


main()
