def solve(N):
    n = N
    digits = set([x for x in str(N)])
    i = 2
    while len(digits) < 10:
        m = N * i
        if n == m:
            return "INSOMNIA"
        n = m
        i += 1
        digits.update([x for x in str(n)])
    return str(n)

file_name = 'A-large.in'

data = []

with open(file_name, 'r') as f:
    T = int(f.readline())
    for i in range(T):
        N = int(f.readline())
        data.append(N);

output = ""
for i, datum in enumerate(data):
    output += "Case #" + str(i + 1) + ": " + solve(datum) + "\n"

print(output)
with open('output', 'w') as f:
    f.write(output)
