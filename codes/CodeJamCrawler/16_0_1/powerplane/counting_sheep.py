#!/usr/bin/env python
import fileinput


def solve(n, max_n=1000000):
    if n == 0:
        return None
    seen = set([])
    for i in range(1, max_n+1):
        s = str(n * i)
        [seen.add(j) for j in s if j not in seen]
        if len(seen) == 10:
            return s
    return None

def main():
    out_tpl = 'Case #{}: {}'
    case_num = -1
    for idx, line in enumerate(fileinput.input()):
        if idx == 0:
            case_num = int(line)
        else:
            num = solve(int(line))
            if not num:
                num = 'INSOMNIA'
            print out_tpl.format(idx, num)

if __name__ == '__main__':
    main()
