import sys

def solve(s):
    r = 1 if s[0] == '-' else 0
    i = 0
    while i < len(s) and s[i] == '-':
        i += 1
    while i < len(s):
        while i < len(s) and s[i] == '+':
            i += 1
        if i < len(s) and s[i] == '-':
            r += 2
        while i < len(s) and s[i] == '-':
            i += 1
    return r

input_file = open(sys.argv[1], "r")
output_file = open(sys.argv[2], "w")

T = int(input_file.readline().strip())
strings = input_file.readlines()
results = []
for s in strings:
    results.append(solve(s.strip()))

for i in xrange(T):
    output_file.write("Case #{0}: {1}\n".format(i+1, results[i]))

input_file.close()
output_file.close()