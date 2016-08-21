sample_input = """5
0
1
2
11
1692
"""

sample_output = """INSOMNIA
10
90
110
5076
"""


def do_one(line):
    num = int(line)

    if num == 0:
        return 'INSOMNIA'

    count = 1
    digits_seen = set(line)
    while len(digits_seen) < 10:
        count += 1
        digits_seen = digits_seen.union(str(num * count))

    return str(num * count)
