#!/usr/bin/env python2.7

import math
import sys


class Result:
    def __init__(self, jam_coin, base_divisors):
        """
        :type jam_coin: str
        :type base_divisors: dict[int, int]
        """
        self.jam_coin = jam_coin
        self.base_divisors = base_divisors

    def __str__(self):
        result = list()
        result.append(self.jam_coin)
        for base in range(2, 11):
            divisor = self.base_divisors.get(base)
            result.append(str(divisor))
        return ' '.join(result)


def challenge(n, j):
    """
    Produce j different jam coins of length n.
    :type n: int
    :type j: int
    :rtype: list[Result]
    """
    results = list()
    max_divisor = int(math.sqrt(2 ** n))
    for inner_bytes in xrange(0, 2 ** (n - 2)):
        sub_coin = format(inner_bytes, 'b').zfill(n - 2)
        jam_coin = '1' + sub_coin + '1'
        base_divisors = find_base_divisors(jam_coin, max_divisor)
        if base_divisors:
            result = Result(jam_coin, base_divisors)
            results.append(result)
            if len(results) >= j:
                break
    return results


def find_base_divisors(jam_coin, max_divisor):
    """
    :type jam_coin: str
    :type max_divisor: int
    :rtype: dict[int, int] | None
    """
    base_divisors = dict()
    for base in range(2, 11):
        value = get_as_base(jam_coin, base)
        divisor = find_divisor(value, max_divisor)
        if not divisor:
            return None
        base_divisors[base] = divisor
    return base_divisors


def find_divisor(value, max_divisor):
    """
    :type value: int
    :type max_divisor: int
    :rtype: int | None
    """
    for divisor in xrange(2, max_divisor):
        if value % divisor == 0:
            return divisor
    return None


def get_as_base(jam_coin, base):
    """
    :type jam_coin: str
    :type base: int
    :rtype: int
    """
    value = 0
    base_value = 1
    for digit in reversed(jam_coin):
        if digit == '1':
            value += base_value
        base_value *= base
    return value


def main(stream):
    """
    :type stream: file
    """
    first_line = stream.readline()
    case_count = int(first_line)
    case_number = 1
    for line in stream:
        case_input = line.strip()
        (n_string, _, j_string) = case_input.partition(' ')
        n = int(n_string)
        j = int(j_string)
        results = challenge(n, j)
        print 'Case #%d:' % case_number
        for result in results:
            print result
        if case_number == case_count:
            break
        else:
            case_number += 1


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        with open(file_name) as file_stream:
            main(file_stream)
    else:
        main(sys.stdin)
