def solve(s):
    s = [i for i in s]
    result = [s[0]]
    s = s[1:]
    for i in s:
        if i>=result[0]:
            result.insert(0, i)
        else:
            result.append(i)
    return ''.join(result)

cases = int(input())
words = [input() for _ in range(cases)]
for i, word in enumerate(words):
    print("Case #{}: {}".format(i+1, solve(word)))