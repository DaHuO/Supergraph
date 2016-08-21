from sys import stdin
from fractions import Fraction


def digit_counter(n, d):
    s = str(n)
    for i in range(len(s)):
        d[s[i]] = True

def all_true(d):
    ans = True
    for _, val in d.items():
        ans = ans and val
    return ans

def solve_test_case(t): 
    ans = ''

    # write your solution here
    n = int(stdin.readline())
    d = dict([(str(k), False) for k in range(10)])

    for l in range(1, 1001):
        h = l * n
        digit_counter(h, d)        
        if all_true(d):
            ans = str(h)
            break

    if not all_true(d):
        ans = 'INSOMNIA'

    # writing answer
    print('Case #%d: %s' % (t, ans))


def main():
    T = int(stdin.readline())
    for t in range(T):
        solve_test_case(t+1)


if __name__ == "__main__":
    main()
