#! /usr/bin/env python
cnt = 0
def is_same(s, i):
    t = s[0]
    for a in xrange(1, i):
        if t != s[a]:
            return False
    return True

def flip(S, i):
    global cnt
    # print S[0:i], list(reversed(S[0:i]))
    # S[0:i] = list(reversed(S[0:i]))
    cnt += 1
    for a in xrange(i+1):
        S[a] = '+' if S[a] == '-' else '-'

def print_answer(i, a):
    print 'Case #{}:'.format(i), a


def solve(t):
    global cnt
    cnt = 0
    S = list(raw_input())
    # print 'in', S
    for i in xrange(len(S)-1):
        if S[i+1] != S[i]:
            flip(S, i)
        # print i, S

    # print 'out', S
    if S[0] == '-':
        cnt+=1

    print_answer(t, cnt)


def main():
    tcase = input()

    for t in xrange(1,tcase+1):
        solve(t)

if __name__ == '__main__':
    main()
