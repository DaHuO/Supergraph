
digits = [0, 2, 4, 6, 5, 1, 7, 8, 9, 3]
words = ["ZERO", "TWO", "FOUR", "SIX", "FIVE", "ONE", "SEVEN", "EIGHT", "NINE", "THREE"]
ch = ["Z", "W", "U", "X", "F", "O", "V", "G", "I", "T"]

def solve():
    line = input()
    chars = {}

    for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        chars[c] = 0

    for c in line:
        chars[c] += 1

    ans = []

    for w, c, d in zip(words, ch, digits):
        n = chars[c]
        ans.extend([d] * n)
        for cc in w:
            chars[cc] -= n

    return "".join(map(str, sorted(ans)))



T = int(input())

for t in range(T):
    ans = solve()
    print("Case #{}: {}".format(t+1, ans)) 