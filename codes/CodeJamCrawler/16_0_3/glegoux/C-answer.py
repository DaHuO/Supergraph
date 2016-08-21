#!/usr/bin/env python3

prims = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,
113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,
233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,
359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,
487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,
619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,
761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,
911,919,929,937,941,947,953,967,971,977,983,991,997]

def is_prime(n):
    for i in prims:
        if n % i == 0:
            return i
    return None

def get_bases(number, N):
    l = []
    for base in range(2, 11):
        l.append(compute(number, base, N))
    return l

def compute(number, base, N):
    n = 0
    for i, digit in enumerate(number):
        n += digit*(base**(N-1-i))
    return n

def is_jamcoin(number, N):
    ps = []
    for n in get_bases(number, N):
        p = is_prime(n)
        if p is None:
            return None
        else:
            ps.append(p)
    return ps

def enum(N, J):
    j = 0
    l = []
    for n in range(1<<N-2):
        if j == J:
            break
        number = list(map(int, bin(n)[2:]))
        number = [0]*(N-2-len(number)) + number
        number.insert(0, 1)
        number.append(1)
        ps = is_jamcoin(number, N)
        if ps is not None:
            l.append("".join(map(str, number)) + " " + " ".join(map(str, ps)))
            j += 1
    return l

def print_answer(n, result):
    res = "\n".join(map(str, result))
    print("Case #{}:\n{}".format(n, res))

def main():
    T = int(input())
    for t in range(T):
        N, J = list(map(int, input().split(' ')))
        print_answer(t + 1, enum(N, J))

if __name__ == "__main__":
    main()
