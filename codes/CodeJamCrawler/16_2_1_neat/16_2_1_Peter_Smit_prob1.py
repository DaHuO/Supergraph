from collections import Counter
import sys

options = [('Z', "ZERO", 0),
           ('G', "EIGTH", 8),
           ('X', "SIX", 6),

           ('U', "FOUR", 4),
           ('W', "TWO", 2),
           ('O', "ONE", 1),

           ('H', "THREE", 3),
           ('F', "FIVE", 5),
           ('S', "SEVEN", 7),

           ('I', "NINE", 9),

           ]

fin = sys.stdin
num_cases = int(fin.readline().strip())

for t in range(num_cases):
    s = fin.readline().strip()

    left = Counter(s)
    numbers = []

    for key, word, num in options:
        for _ in range(left[key]):
            numbers.append(num)
            left -= Counter(word)

    print("Case #{}: {}".format(t+1, "".join(str(i) for i in sorted(numbers))))