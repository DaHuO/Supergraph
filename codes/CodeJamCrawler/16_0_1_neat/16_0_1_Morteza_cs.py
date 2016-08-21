import os
import sys


def main():
    count = int(input())
    for i in range(count):
        n = int(input())
        insomnia = 1
        dic = {}
        for j in range(1,20000):
            t = n*j
            for s in str(t):
                # print(s, end=' ')
                dic[s] = 1
            # print('')
            if len(dic) == 10:
                insomnia = 0
                break
        print('Case #{}: {}'.format(i+1, 'INSOMNIA' if insomnia == 1 else t))

if __name__ == '__main__':
    main()
