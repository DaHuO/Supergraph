import sys

def solve(n):
    if n == 0:
        return "INSOMNIA"
    digits = [0]* 10
    t = n

    while True:
        m = t
        while m != 0:
            digits[m % 10] = 1
            m /= 10
        if not 0 in digits:
            break
        t += n
    return t

input_file = open(sys.argv[1], "r")
output_file = open(sys.argv[2], "w")

T = int(input_file.readline().strip())
strings = input_file.readlines()
results = []
for s in strings:
    results.append(solve(int(s.strip())))

for i in xrange(T):
    output_file.write("Case #{0}: {1}\n".format(i+1, results[i]))

input_file.close()
output_file.close()