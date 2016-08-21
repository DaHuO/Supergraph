def iterate(filename):
    fileling = open(filename)
    num_cases = int(fileling.readline())
    for case_num in range(num_cases):
        seq = fileling.readline().rstrip()
        print "Case #" + str(case_num + 1) + ':', process(seq)


def process(seq):
    seq = turn_bin(seq)
    flips = 0
    while not (sum(seq) == 0 or sum(seq) == len(seq)):
        for index in range(len(seq) - 1):
            if seq[index] != seq[index + 1]:
                seq = seq[index + 1:]
                flips += 1
                break
    if sum(seq) == 0:
        flips += 1
    return flips


def turn_bin(seq):
    res = list()
    for char in seq:
        if char == '+':
            res.append(1)
        else:
            res.append(0)
    return res


if __name__ == '__main__':
    iterate('B-large.in')
