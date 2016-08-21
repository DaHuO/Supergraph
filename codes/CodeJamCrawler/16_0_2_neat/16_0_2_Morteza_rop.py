import os
import sys


def main():
    count = int(input())
    for i in range(count):
        stack = input()
        mane = 0
        pre = stack[0]
        for sign in stack:
            if sign != pre:
                mane += 1
            pre = sign
        if stack[-1] == '-':
            mane += 1

        print('Case #{}: {}'.format(i + 1, mane))

if __name__ == '__main__':
    main()
