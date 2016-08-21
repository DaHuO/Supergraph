def expand_str(string):
    return '0' + ''.join([s + s for s in string]) + '0'

def check_div(string):
    for b in range(3, 12):
        number = int(string, b)
        assert number % (b + 1) == 0

def C(N, J):
    pairs = (N - 2) / 2
    max_num = 2 ** pairs
    s = '1' + ''.join(['0' for _ in xrange(N-2)]) + '1'
    for i in xrange(max_num):
        bin_str = "{0:b}".format(i)
        bin_str = ''.join(['0' for _ in range(pairs - len(bin_str))]) + bin_str
        exp = expand_str(bin_str)
        exp = ''.join([str(int(exp[j]) or int(s[j])) for j in range(len(s))])
        print exp, '3', '4', '5', '6', '7', '8', '9', '10', '11'
        check_div(exp)
        if i == J - 1:
            return