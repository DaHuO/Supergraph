#!/bin/python

import math

#N = 16
#J = 50

# large
#N = 32
#J = 500

# generate numbers of len=K with size of J

"""
K = 3

initial = '101'
result = []
while len(result) < J:
    correct = True
    middle = initial
    for i in range(2, 11):
        divsor = find_divsor(int(initial, i)):
        middle += ' ' + str(divsor)
        if not divsor:
            correct = False
            break

    if correct:
        result.append(middle)
"""


def find_divsor(n):
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            return i
        if i > 1000000:
            return None
    return None


def effort(n):
    rep = bin(n)[2:]
    result = rep
    for i in range(2, 11):
        d = find_divsor(int(rep, i))
        if d:
            result += ' ' + str(d)
        else:
            return None
    return result


def get_next(n):
    return n + 2


def generate_results(N, J):
    result = []
    zeros = '0' * (N-2)
    number = int('1' + zeros + '1', 2)
    while J > 0:
        #print("J " + str(J) + " -> " + str(number))
        e = effort(number)
        if e is not None:
            result.append(e)
            J -= 1
        number = get_next(number)


    return result



T = int(input())
for i in range(T):
    N, J = list(map(int, input().split()))


    print("Case #" + str(i+1) + ":")
    results = generate_results(N, J)
    for r in results:
        print(r)
