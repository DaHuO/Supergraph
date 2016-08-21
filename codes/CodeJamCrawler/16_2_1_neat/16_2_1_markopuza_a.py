digs = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def find(x):
    if sum(x) == 0:
        return []

    for i in range(10):
        copy = list(x)
        found = True
        for letter in digs[i]:
            if copy[ord(letter) - ord('A')] == 0:
                found = False
                break
            else:
                copy[ord(letter) - ord('A')] -= 1
        if not found:
            continue
        rec = find(copy)
        if rec == -1:
            continue
        else:
            return [i] + rec
    return -1

for t in range(1,int(input())+1):
    s = [0 for _ in range(26)]
    for letter in input():
        s[ord(letter) - ord('A')] += 1
    print('Case #' + str(t) + ': ' + ''.join(map(str,sorted(find(s)))))
