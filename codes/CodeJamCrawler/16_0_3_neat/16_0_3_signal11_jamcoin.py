import sys

#
# a simple gray code generator.
#
def barrier():
    while True:
        yield False

def troll(a, i):
    previous = troll(a, i - 1) if i > 0 else barrier()
    while True:
        a[i] = 1 - a[i]
        yield True
        yield next(previous)

def setup(n):
    a = [0] * n
    lead_coroutine = troll(a, n - 1)
    return a, lead_coroutine

def gray(n):
    a, lead = setup(n)
    yield a
    while next(lead):
        yield a

#
# use 'factor' to do the heavy lifting
#
def factorize_jamcoins(jamcoin_list):
    import subprocess

    factor_command_list = 'factor'
    jamcoin_factors = []

    for jc_value in jamcoin_list:
        factor_command_list += ' ' + str(jc_value)

    #print "running-command: '" + factor_command_list + "'"
    jc_factorized = subprocess.Popen(factor_command_list, stdout = subprocess.PIPE, shell = True)
    jc_factorized.wait()

    #
    # 'factor' factorizes a number 'N' and dumps it's output
    # in the following format:
    #      N: F1 F2 F3 ... Fn
    # factor_list is just a list of this output i.e.
    #    ['N:', 'F1', 'F2', ... 'Fn']
    #
    for line in jc_factorized.stdout:
        factor_list = line.rstrip('\n').split(' ')
        jamcoin_factors.append(factor_list)

    return jamcoin_factors

def validate_jamcoin_factors(jamcoin_factor_list):
    '''
    this just goes over the jamcoin_factors and returns 'True'
    if there are more than 1 factors for all numbers in the jamcoin...
    '''
    for l in jamcoin_factor_list:
        #
        # each 'l' corresponds to the factor of a number in a given
        # base. and has the following format:
        #    ['N:', 'F1', 'F2', ... 'Fn']
        #
        # thus, all non-prime jamcoins, have >= 3 factors...
        if len(l) < 3:
            return False

    return True

def get_first_jamcoin_factor_str(jc_factor_list):
    first_factor = []
    for fl in jc_factor_list:
        first_factor.append(fl[1])
    first_factor_str = ' '.join(f for f in first_factor)
    return first_factor_str

def generate_jam_coins(len, count):
    iter = 1
    for G in gray(len - 2):
        tmp_jc = list(G)

        # all jam-coins begin and end with '1'
        tmp_jc.insert(0, 1)
        tmp_jc.append(1)

        tmp_jc_str = ''.join(str(x) for x in tmp_jc)
        tmp_jc_numbers = []
        for base_num in xrange(2, 11):
            tmp_jc_numbers.append(int(tmp_jc_str, base_num))

        jamcoin_factors = factorize_jamcoins(tmp_jc_numbers)
        if validate_jamcoin_factors(jamcoin_factors) == True:
            print tmp_jc_str + ' ' + get_first_jamcoin_factor_str(jamcoin_factors)
            iter += 1

        if iter > count:
            break
    return

def main():
    num_tests = int(sys.stdin.readline())
    for tc in xrange(1, num_tests+1):
        N, J = [int(s) for s in raw_input().split(" ")]
        print "Case #" + str(tc) + ": "
        generate_jam_coins(N, J)

    return


# start it all
if __name__ == "__main__":
    main()
