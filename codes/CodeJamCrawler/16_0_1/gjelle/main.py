#!/usr/bin/env python2.7

import sys


def challenge(initial):
    """
    :type initial: str
    :rtype: str
    """
    n = int(initial)
    if n == 0:
        return 'INSOMNIA'
    remaining = set('0123456789') - set(initial)
    y = n
    while remaining:
        y += n
        digits = set(str(y))
        remaining -= digits
    return y


# def challenge(initial):
#     """
#     :type initial: str
#     :rtype: str
#     """
#     n = int(initial)
#     remaining = set('0123456789') - set(initial)
#     history = list()
#     y = n
#     while remaining:
#         y += n
#         digits = set(str(y))
#         normalized_digits = "".join(sorted(digits))
#         if normalized_digits in history:
#             return 'INSOMNIA'
#         else:
#             remaining -= digits
#             history.append(normalized_digits)
#     return y


def main(stream):
    """
    :type stream: file
    """
    first_line = stream.readline()
    case_count = int(first_line)
    case_number = 1
    for line in stream:
        n = line.strip()
        result = challenge(n)
        print 'Case #%(case_number)d: %(result)s' % dict(
            case_number=case_number,
            result=result
        )
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
