#!/usr/bin/env python
# -*- coding: utf-8 -*-

MAX_DIVISOR = 11

def get_divisor(number):
    for i in xrange(2, MAX_DIVISOR + 1):
        if not number % i:
            return i

    return None


def get_divisors(coin):
    divisors = []

    for base in xrange(2, 11):
        number = int(coin, base)
        divisor = get_divisor(number)
        if divisor:
            divisors.append(divisor)
        else:
            return None

    return divisors


def generate_jamcoin(n):
    for i in xrange(pow(2, n - 2)):
        coin = "{0:#b}".format(i)[2:].zfill(n - 2)
        coin = "1{0}1".format(coin)
        divisors = get_divisors(coin)
        if divisors:
            yield coin, divisors


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, j = [int(s) for s in raw_input().split(" ")]
  print "Case #{0}:".format(i)
  for jamcoin, divisors in generate_jamcoin(n):
    print jamcoin, ' '.join([str(divisor) for divisor in divisors])
    j -= 1
    if not j:
        exit()
