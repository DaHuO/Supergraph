# coding: UTF-8

import collections

def main():
    T = int(input())
    for case in range(1, T + 1):
        n = int(input())
        c = []
        for i in range(2*n-1):
            ary = map(int, input().split())
            c.extend(ary)
        c = collections.Counter(c)

        ans = []
        for k, v in c.items():
            if v % 2 == 1:
                ans.append(k)
        ans.sort()
        ans = map(str, ans)

        print('Case #{}: {}'.format(case, ' '.join(ans)))

if __name__ == '__main__':
    main()
