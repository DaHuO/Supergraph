#Uses python3
import sys
import time
import random

"""
@author Daniel Flores
@date 8/04/2016
"""

def counting_sheep_naive(N):

    if(N<=0):
        return "INSOMNIA"

    d = [False] * 10
    N = N
    i = 1
    sleep = False
    n = None

    while not sleep:
        n = N * i
        digits = list(map(int, str(n)))
        for j in range(0, len(digits)):
            d[digits[j]] = True
        if False not in d:
            sleep = True
        else:
            i += 1

    return str(n)

def generate(size):
    a = []
    while len(a) < size:
        n = random.randint(0, 10**6)
        a.append(n)
    return a

def test():

    start = time.time()

    print("================")
    cases = generate(1000)
    print(cases)
    for i in range(0,len(cases)):
        print("Case #" + str(i+1) + ": " + counting_sheep_naive(cases[i]))
    print("================")

    end = time.time()
    print("Time : " + str(end - start))


if __name__ == '__main__':

    #test()
    f = open('output', 'w')
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    T = data[0]
    for i in range(1,T+1):
        if(i == T):
            f.write("Case #" + str(i) + ": " + counting_sheep_naive(data[i]))
        else:
            print("Case #" + str(i) + ": " + counting_sheep_naive(data[i]), file=f)
