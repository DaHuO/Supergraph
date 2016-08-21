def solve(S):
    d = '+'
    c = 0
    for p in reversed(S):
        if p != d:
            d = '-' if d == '+' else '+'
            c += 1
    return str(c)

file_name = 'B-large.in'

data = []

with open(file_name, 'r') as f:
    T = int(f.readline())
    for i in range(T):
        S = f.readline().strip()
        data.append(S);

output = ""
for i, datum in enumerate(data):
    output += "Case #" + str(i + 1) + ": " + solve(datum) + "\n"

print(output)
with open('output', 'w') as f:
    f.write(output)
