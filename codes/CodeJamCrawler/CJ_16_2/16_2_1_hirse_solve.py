from collections import Counter

digit_names = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
u_order = [0, 2, 4, 6, 3, 1, 5, 7, 8, 9]


def solve(S):
    c = Counter(S)
    digits = []
    for i in u_order:
        digit_name = digit_names[i]
        cs = [c[letter] for letter in digit_name]
        max_occurence = min(cs)
        for letter in digit_name:
            c[letter] -= max_occurence
        digits += [i] * max_occurence
        
    print(sum(c.values()))
    return "".join([str(x) for x in sorted(digits)])


file_name = 'A-large.in'

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
