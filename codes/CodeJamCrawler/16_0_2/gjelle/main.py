#!/usr/bin/env python2.7

import sys


def challenge(stack):
    """
    :type stack: str
    :rtype: str
    """
    flip_count = 0
    top = stack[0]
    for pancake in stack[1:]:
        if pancake != top:
            flip_count += 1
            top = pancake
    if top != '+':
        flip_count += 1
    return flip_count


def main(stream):
    """
    :type stream: file
    """
    first_line = stream.readline()
    case_count = int(first_line)
    case_number = 1
    for line in stream:
        case_input = line.strip()
        result = challenge(case_input)
        print 'Case #%(case_number)d: %(result)d' % dict(
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
