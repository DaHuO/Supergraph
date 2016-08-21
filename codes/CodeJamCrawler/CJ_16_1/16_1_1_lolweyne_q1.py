def winningLastWord(n):
    n = [i for i in n]
    result = [n[0]]
    n = n[1:]
    for i in n:
        if i>=result[0]:
            result.insert(0, i)
        else:
            result.append(i)
    return ''.join(result)

case = int(input())
word = [input() for i in range(case)]
for i, n in enumerate(word):
    print("Case #{}: {}".format(i+1, winningLastWord(n)))
