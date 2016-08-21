#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return [2]
    if all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2)):
        return []

    a = []
    i = 3
    while True:
        if n % i == 0:
            a.append(i)
            break
        i += 2
    return a

import string
BASE_LIST = string.digits + string.letters + '_@'
BASE_DICT = dict((c, i) for i, c in enumerate(BASE_LIST))

def base_decode(string, reverse_base=BASE_DICT):
    length = len(reverse_base)
    ret = 0
    for i, c in enumerate(string[::-1]):
        ret += (length ** i) * reverse_base[c]
    return ret

def base_encode(integer, base=BASE_LIST):
    length = len(base)
    ret = ''
    while integer != 0:
        ret = base[integer % length] + ret
        integer /= length
    return ret

if __name__ == "__main__":
    testcases = input()
     
    for caseNr in xrange(1, testcases+1):

        print ("Case #%i:" % (caseNr))

        cipher = raw_input()
        cipher_input = cipher.split(' ')
        N = int(cipher_input[0])
        J = int(cipher_input[1])

        stop = ''
        for i in range(0, N): 
            stop = '%s1' % (stop)

        results = []
        number = 0
        while True:
            base_ = base_encode(number, base=BASE_LIST[:2])
            ans = '1%s1' % base_.zfill(N-2)
            is_prime_ans = False

            nontrivial_seq = []
            for i in range(2, 11):
                BASE_DICT = dict((c, i) for i, c in enumerate(BASE_LIST[:i]))
                base_number = base_decode(ans, BASE_DICT)
                numbers = is_prime(base_number)
                if len(numbers) == 0:
                    is_prime_ans = True
                    break
                else:
                    divisors = numbers
                    nontrivial = divisors[0]
                    nontrivial_seq.append(nontrivial)

            number += 1
            if is_prime_ans:
                if ans == stop:
                    break
                else:
                    continue
            results.append({
                'jamcoin': ans,
                'nontrivial': nontrivial_seq
            })

            print ("%s %s" % (ans, ' '.join(map(str, nontrivial_seq))))
            if len(results) >= J:
                break
                
            if ans == stop:
                break



