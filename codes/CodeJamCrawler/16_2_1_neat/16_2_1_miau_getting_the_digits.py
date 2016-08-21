from toolz import countby

rules = [
    # (digit, check_char, map)
    ('0', 'Z', {'Z': 1, 'O': 1, 'R': 1, 'E': 1}),
    ('2', 'W', {'T': 1, 'W': 1, 'O': 1}),
    ('4', 'U', {'O': 1, 'R': 1, 'U': 1, 'F': 1}),
    ('6', 'X', {'I': 1, 'S': 1, 'X': 1}),
    ('8', 'G', {'G': 1, 'H': 1, 'I': 1, 'T': 1, 'E': 1}),
    ('5', 'F', {'V': 1, 'I': 1, 'F': 1, 'E': 1}),          # (after 4)
    ('7', 'V', {'V': 1, 'S': 1, 'N': 1, 'E': 2}),          # (after 5)
    ('9', 'I', {'I': 1, 'N': 2, 'E': 1}),                  # (after 6, 8, 5)
    ('1', 'O', {'O': 1, 'N': 1, 'E': 1}),                  # (after 0, 2, 4)
    ('3', 'H', {'T': 1, 'H': 1, 'R': 1, 'E': 2}),          # (after 8)
]

def main():
    # for s in ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"):
    #     print(countby(lambda x: x, sorted(s)))
    cases = int(input())
    for case in range(cases):
        (s,) = input().split()
        result = solve(s)
        print("Case #%d: %s" % (case + 1, result))

def solve(s):
    result = ""
    count = countby(lambda x: x, s)
    for digit, check_char, map in rules:
        # print(count)
        # print(digit, check_char, map)
        if check_char in count and count[check_char] > 0:
            n = count[check_char]
            for k, v in map.items():
                count[k] -= v * n
            result += digit * n
    return "".join(sorted(result))

main()
