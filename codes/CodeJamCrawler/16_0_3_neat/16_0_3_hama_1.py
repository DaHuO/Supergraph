import math

def find_divider(n):
    if n % 2 == 0 and n > 2:
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return -1

def to_int_with_base(string, base):
    ret = 0
    for i in range(len(string)):
        if string[i] == "1":
            ret += base ** (len(string)-1-i)
    return ret

def gen_string(index, length):
    format_rule = "0" + str(length-2) + "b"
    return "1" + format(index, format_rule) + "1"

fin = open("small.in", 'r')
fout = open("small.out", 'w')

t = int(fin.readline())

for cases in range(1, t+1):
    raw_in = fin.readline().split()
    jamcoin_length, jamcoin_count = int(raw_in[0]), int(raw_in[1])
    fout.write("Case #%d:\n" % cases)

    jamcoins = 0
    for i in range(2**(jamcoin_length-2)):
        if jamcoins >= jamcoin_count:
            break
        candidate = gen_string(i, jamcoin_length)
        dividers = []
        for j in range(2, 11):
            divider = find_divider(to_int_with_base(candidate, j))
            if divider == -1:
                break
            dividers.append(divider)
        if len(dividers) == 9:
            # Candidate is jamcoin!
            jamcoins += 1
            fout.write("%s %s\n" % (candidate, ' '.join(map(str, dividers))))

fin.close()
fout.close()
