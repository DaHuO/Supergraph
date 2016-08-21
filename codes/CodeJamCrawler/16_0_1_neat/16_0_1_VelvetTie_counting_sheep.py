#import doctest

def name_numbers(N):
    """
    Name numbers until all digits from 0 to 9 have been counted.

    >>> name_numbers(0)
    0

    >>> name_numbers(1)
    10
    >>> name_numbers(2)
    90
    >>> name_numbers(11)
    110
    >>> name_numbers(1692)
    5076
    """
    digits = [0 for tmp in range(10)]
    ndigits = 0


    if N == 0:
        return N
    i = 1
    num = 0
    while ndigits < 10:
        num = i * N
        quotient = num
        # Count the digits in num.
        while quotient > 0:
            #print("quotient={}".format(quotient))
            # Extract a digit.
            remainder = quotient % 10
            #print(remainder)
            # If the digit has not been seen before, indicate that it has now been seen,
            if digits[remainder] == 0:
                digits[remainder] = 1
                ndigits += 1

            quotient //= 10
        i += 1
    return num

def read_input():
    t = int(input())
    for test_num in range(1, t + 1):
        N = int(input())
        output = name_numbers(N)
        if output == 0:
            output = "INSOMNIA"
        print("Case #{}: {}".format(test_num, output))

if __name__ == "__main__":
    read_input()






