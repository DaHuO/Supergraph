#!/usr/bin/python

def solve(string):
    start = string[0]
    result = [start]
    for s in string[1:]:
        if s >= result[0]:
            result.insert(0, s)
        else:
            result.append(s)
    return ''.join(result)


def main():
    t = int(input())
    for i in range(1, t + 1):
        string = input().strip()
        print('Case #{}: {}'.format(i, solve(string)))


if __name__ == '__main__':
    main()
