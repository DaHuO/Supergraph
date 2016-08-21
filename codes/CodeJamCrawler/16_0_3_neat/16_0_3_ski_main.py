smallprimes = [
    2,    3,    5,    7,   11,   13,   17,   19,   23,   29, 
   31,   37,   41,   43,   47,   53,   59,   61,   67,   71, 
   73,   79,   83,   89,   97,  101,  103,  107,  109,  113, 
  127,  131,  137,  139,  149,  151,  157,  163,  167,  173, 
  179,  181,  191,  193,  197,  199,  211,  223,  227,  229, 
  233,  239,  241,  251,  257,  263,  269,  271,  277,  281, 
  283,  293,  307,  311,  313,  317,  331,  337,  347,  349, 
  353,  359,  367,  373,  379,  383,  389,  397,  401,  409, 
  419,  421,  431,  433,  439,  443,  449,  457,  461,  463, 
  467,  479,  487,  491,  499,  503,  509,  521,  523,  541, 
  547,  557,  563,  569,  571,  577,  587,  593,  599,  601, 
  607,  613,  617,  619,  631,  641,  643,  647,  653,  659, 
  661,  673,  677,  683,  691,  701,  709,  719,  727,  733, 
  739,  743,  751,  757,  761,  769,  773,  787,  797,  809, 
  811,  821,  823,  827,  829,  839,  853,  857,  859,  863, 
  877,  881,  883,  887,  907,  911,  919,  929,  937,  941, 
  947,  953,  967,  971,  977,  983,  991,  997, 1009, 1013, 
]


def find_divisor(n):
    for p in smallprimes:
        if n % p == 0:
            return p


def make_coins(N, J):
    """
    N - coin digit length
    J - how many coins to make
    """
    coin = int('1' * (N-1), 2)
    j = 0

    while True:
        coin = coin + 2
        divs = []

        for s in range(2, 11):
            n = int(bin(coin)[2:], s)
            d = find_divisor(n)
            if d:
                divs.append(d)
            else:
                break
        else:
            bincoin = bin(coin)[2:]
            assert_coin(N, bincoin, divs)
            print bincoin, ' '.join(map(str, divs))
            j += 1
            if j == J:
                return


def assert_coin(N, bincoin, divs):
    assert len(bincoin) == N, bincoin
    assert len(divs) == 9, divs
    assert bincoin.endswith('1'), bincoin
    assert bincoin.startswith('1'), bincoin
    for base, d in enumerate(divs, 2):
        n = int(bincoin, base)
        assert n % d == 0, (n, d)


def parse_file(lines):
    for i, case in enumerate(lines[1:], 1):
        N, J = map(int, case.strip().split())
        print 'Case #%d:' % i
        make_coins(N, J)


if __name__ == '__main__':
    import sys
    args = sys.argv[1:]

    if len(args) == 2:
        make_coins(int(args[0]), int(args[1]))

    elif len(args) == 1:
        infile = args[0]
        outfile = args[0].replace('.in', '') + '.out'
        with open(infile) as f:
            lines = list(f)
        with  open(outfile, 'w') as out:
            sys.stdout = out
            parse_file(lines)
