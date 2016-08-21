# 2016-QR-C: Coin Jam

import math

def base_to_int(s_num, i_base):
    """Convert the string representation to int in base.
    limits: 2 <= base <= 10
    """
    # build the integer value starting with the least significant digit
    val = 0
    for place_value, sym in enumerate(reversed(list(s_num))):
        val += int(sym) * (i_base ** place_value)
    return val


def factor(i_num):
    """Determine whether the input is prime.
    Return a factor for num (1 < factor < num)
    Return False if num is prime.
    """
    # The largest facter we need to check is sqrt of num
    i_max = int(math.sqrt(i_num)) + 1
    # To save time, we limit the search; there are plenty of non-prime numbers
    i_max = min(i_max, 1000)
    # For simplicity, we always return the smallest/first factor
    for i in xrange(2, i_max):
        if i_num % i == 0:
            return i
    # it is prime
    return False


def generate_options(i_len):
    """Generate unique coins.
    Generated in order for simplicity
    """
    # the first and last digits are always 1, so we need len-2 additional digits
    need_len = (i_len - 2)
    for i in xrange(2 ** need_len):
        yield "1{0:0{width}b}1".format(i, width=need_len)


def is_jamcoin(s_coin):
    # Keep track of the output. Output is printed only if this is a jamcoin.
    output = [s_coin]
    for base in range(2, 10 + 1):
        i_value = base_to_int(s_coin, base)
        i_factor = factor(i_value)
        if not i_factor:
            # Fail this coin
            return False
        # Pass this base. Record the factor.
        output.append(i_factor)
    # It is a jamcoin. Display the output
    print " ".join([str(s) for s in output])
    return True


def generate_answers(i_len, i_howmany):
    i_found = 0
    for s_option in generate_options(i_len):
        if is_jamcoin(s_option):
            i_found += 1
        if i_found >= i_howmany:
            break


def main():
    num_cases = int(raw_input())
    for case_id in xrange(num_cases):
        (i_len, i_howmany) = [int(s) for s in raw_input().split(" ")]
        print "Case #{0}:".format(case_id + 1)
        generate_answers(i_len, i_howmany)


if __name__ == "__main__":
    main()
