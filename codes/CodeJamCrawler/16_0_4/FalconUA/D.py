from sys import stdin
from fractions import Fraction


def solve_test_case(t): 
    ans = ''
    # write your solution here
    K, C, S = [int(i) for i in stdin.readline().split()]
    if S >= K:
        ans = ' '.join([str(i * (K**(C-1)) + 1) for i in range(S)])
    else:
        ans = 'IMPOSSIBLE'

    # outputting answer
    print('Case #%d: %s' % (t, ans))


def main():
    T = int(stdin.readline())
    for t in range(T):
        solve_test_case(t+1)

if __name__ == "__main__":
    main()
