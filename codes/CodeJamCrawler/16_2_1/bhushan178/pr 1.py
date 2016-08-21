digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
freq = [0] * 26

t = int(input())
for x in range(t):
    s = input()
    freq = [0] * 26
    for c in s:
        freq[ord(c) - ord('A')] += 1

    ch = "ZWUFXSGITO"
    dg = [0, 2, 4, 5, 6, 7, 8, 9, 3, 1]

    no = ""
    for i in range(10):
        cnt = freq[ord(ch[i]) - ord('A')]
        no += str(dg[i]) * cnt
        for c in digits[dg[i]]:
            freq[ord(c) - ord('A')] -= cnt
                 
    print('Case #', x + 1, ': ', ''.join(sorted(no)), sep = '')
