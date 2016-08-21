#!/usr/bin/env python

from collections import Counter

numbers = map(Counter,
        ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE'])


def contains(counter, number):
    return all([count >= 0 for count in (counter - number).values()])


def digits(letters):
    q = [(Counter(letters), [], 0)]
    while q:
        counter, phone, last = q.pop(0)
        if not counter:
            return ''.join(map(str, phone))
        for d in range(last, 10):
            if contains(counter, numbers[d]):
                q.append((counter - numbers[d], phone + [d], d))
    return ''


def main():
    T = int(raw_input())
    for i in range(T):
        print 'Case #%s: %s' % ((i+1), digits(raw_input()))


if __name__ == "__main__":
    main()
