
def last_word(s):
    result = [s[0]]

    for ch in s[1:]:
        if ch < result[0]:
            result.append(ch)
        else:
            result.insert(0, ch)

    return ''.join(result)

n = int(input())
for i in range(1, n + 1):
    print('Case #' + str(i) + ':', last_word(input()))


