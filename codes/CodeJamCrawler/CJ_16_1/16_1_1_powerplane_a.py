#!/usr/bin/env python
import fileinput
import itertools

def solve(s):
    anchor = s[0]
    ret = str(anchor)
    greatest = s[0]
    for ch in s[1:]:
        if ch < ret[0]:
            ret += ch
        else:
            ret = ch + ret

    return ret

def main():
    tpl = 'Case #{}: {}'
    case_num =  -1
    for idx, line in enumerate(fileinput.input()):
        if idx == 0:
            case_num = int(line)
        else:
            print tpl.format(idx, solve(line.strip()))

if __name__ == '__main__':
    main()
