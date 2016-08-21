import math

def parse_input(items):
    return int(items[0]), int(items[1])

def get_number_base(number, base):
    x = bin(number)
    result = 0L
    for i in x:
        result *= base
        if i == '1':
            result += 1
    return result

def get_factor(number):
    for i in [2, 3, 5, 7]:
        if number % i == 0:
            return i
    return 1
    """
    root = int(math.sqrt(number))
    i = 2L
    while i <= root:
        if number % i == 0:
            return i
        i += 1
    return 1
    """

def gen_coin_jam(result, number):
    factors = list()
    base = 2L
    while base <= 10L:
        number_base = get_number_base(number, base)
        nontrival_factor = get_factor(number_base)
        if nontrival_factor == 1:
            return
        factors.append(nontrival_factor)
        base += 1
    result.append((bin(number)[2:], factors))

def run(items):
    N, J = parse_input(items)
    #print N, J

    if N <= 2:
        return ""

    total_number = pow(2, N - 2)
    result = list()
    i = 0
    while i <= total_number:
        number = (1 << N - 1) + (i << 1) + 1
        gen_coin_jam(result, number)
        if len(result) == J:
            break
        i += 1
    return result


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    items = raw_input().split(" ")
    result = run(items)
    print "Case #{}:".format(i)
    for coin_jam, factors in result:
        print coin_jam,
        for factor in factors:
            print factor,
        print
    # check out .format's specification for more formatting options
