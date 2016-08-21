#!/usr/bin/env python3


import multiprocessing as mp
import random
import sympy


N = 32
J = 500


def gen(size):
    coin = [1] + [random.choice([0, 1]) for _ in range(size-2)] + [1]
    factors = []
    for base in range(2, 11):
        value = sum(base**power for power, digit in enumerate(coin) if digit)
        factor = find_factor(value)
        if factor is None:
            return None
        factors.append(factor)
    return ''.join(map(str, reversed(coin))), factors


def find_factor(n):
    factors = sympy.ntheory.factorint(n)
    for factor in factors:
        if factor == 1 or factor == n:
            continue
        return factor
    return None


def process(size, queue, flag):
    while flag.value:
        result = gen(size)
        if result is not None:
            queue.put_nowait(result)


def main(size):
    queue = mp.Queue()
    flag = mp.Value('b', 1, lock=False)
    processes = []
    for i in range(mp.cpu_count()):
        p = mp.Process(target=process, args=(size, queue, flag))
        p.start()
        processes.append(p)

    answers = {}
    print('Case #1:', flush=True)
    while len(answers) < J:
        coin, factors = queue.get()
        if coin not in answers:
            answers[coin] = factors
            print(coin, *factors, flush=True)

    flag.value = 0
    for p in processes:
        p.join()


if __name__ == '__main__':
    main(N)
