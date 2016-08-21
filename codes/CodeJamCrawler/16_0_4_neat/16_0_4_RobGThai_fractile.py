def case_number(pos):
    return pos + 1

def print_case(case_no, value):
    print 'Case #{case_no}: {value}'.format(case_no = case_no, value=value)

def clean_line(line):
    return line.replace('\r', '').replace('\n', '')

def simple(case, K, C, S):
    max = S
    simplified = [str(n) for n in xrange(1, max+1)]

    print_case(case_number(case), ' '.join(simplified))

def random(case, K, C, S):
    if K < C:
        max = K
        print_case(case_number(case), K)
    elif K == C:
        simplified = [str(n) for n in xrange(1, K+1)]
        print_case(case_number(case), ' '.join(simplified))
    else:
        max = (K - C) + 1
        answer = []

        for i in xrange(1, S + 1):
            answer += str((K * i) - i)

        print_case(case_number(case), ' '.join(list(set(answer))))

def begin(file):
    with open(file) as input:
        input_size = long(input.readline())
        for case, line in enumerate(input):
            data = clean_line(line).split(' ')
            K, C, S = int(data[0]), int(data[1]), int(data[2])

            # print case+1, '====', K, C, S, K < C
            # generate_pattern(K, C)
            simple(case, K, C, S)
            # random(case, K, C, S)
            # print ''
            # print ''
            # print ''
            # process(no, int(data[0]), int(data[-1]))

def generate_binaries(size, value):
    # print 'Gen', size, value
    return '{val:0>{max}b}'.format(val=value, max=size) \
                             .replace('1','L') \
                             .replace('0','G')

def generate_pattern(p_length ,c=1):
    k = p_length
    orig = None
    for i in xrange(0, 2**k):
        # print i
        n = generate_binaries(p_length, i)
        if not orig: orig = n
        k = n
        for i in range(1, c):
            k = k.replace('G','G' * len(n)).replace('L',n)

        print n, ':', k

if __name__ == '__main__':
    # print generate_binaries(3, 0)
    begin('fractile/D-small-attempt2.in')
