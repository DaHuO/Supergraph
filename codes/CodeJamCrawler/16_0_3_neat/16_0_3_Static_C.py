# -*- coding: utf-8 -*-
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def load_file(filename):
    in_file = open(filename, encoding='utf-8')
    content = in_file.readlines()
    return content

def writeStringToFile(output, filename):
    out_file = open(filename + '.out', 'w')
    for i in output:
        out_file.write(i + '\n')
    out_file.close()

def prime_or_divisor(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return 2
    if n < 9: return True
    if n % 3 == 0: return 3
    r = int(n**0.5)
    f = 5
    while f <= r:
#        print(f)
        if n % f == 0: return f
        if n % (f+2) == 0: return f+2
        f +=6
    return True

def solve(line):
    size = int(line.split()[0])
    j = int(line.split()[1])
    low_limit = 2**(size-1) + 1
    high_limit = 2**size - 1
    jamcoins = []
    for i in range(low_limit, high_limit):
        num_str = "{0:b}".format(i)
        if num_str[len(num_str) - 1] == '0':
        	continue
        is_jamcoin = True
        proof = ""
        for base in range(2, 10 + 1):
            num = int(num_str, base)
            result = prime_or_divisor(num)
            if result == True:
                is_jamcoin = False
            else:
                proof += str(result) + " "
        if is_jamcoin == True:
            jamcoins.append([i, proof])
#            print("found jamcoin", len(jamcoins), i)
            if len(jamcoins) == j:
                return jamcoins
    return "error"

if __name__ == "__main__":
    filename = "C-small-attempt0.in"
    file = load_file(filename)
    n = int(file[0])
#    print(int(file[0]))
    out = []
    line = file[1]
    out.append("Case #1:")
    for i in solve(line):
    	out.append("{:b} {}".format(i[0], i[1].strip()))
#print(out)
writeStringToFile(out, filename)



