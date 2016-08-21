def split_digits(n):
    if n < 10:
        return [n]
    return split_digits(n//10) + [n%10]
def convert(num, b):
    n = 0
    for d in split_digits(num):
        n = b * n + d
    return n
def generate_multiples():
    multiple_list = []
    for i in range(2**15):
        x = '{0:b}'.format(i)
        x = "".join([c*2 for c in x])
        if len(x) != 30:
            x = (30 - len(x))*'0' + x
        multiple_list.append(int('1' + x + '1'))
    return multiple_list

in_file, out_file = open('C-large.in', 'r'), open('C-large.out', 'w')

num_cases = int(in_file.readline())
for case_num in range(num_cases):
    out_file.write("Case #" + str(case_num+1) + ":\n")
    N, J = [int(i) for i in in_file.readline().split()]
    i = 10**(N-1) + 1
    eleven_multiples = generate_multiples()
    for multiple in eleven_multiples:
        is_jamcoin = True
        for base in range(2,11):
            converted = convert(multiple, base)
            if converted%(base+1) != 0:
                is_jamcoin = False
                break
        if is_jamcoin:
            out_file.write(" ".join([str(i) for i in [multiple, 3, 4, 5, 6, 7, 8, 9, 10, 11]] + ['\n']))
            J = J - 1
        if J == 0:
            break